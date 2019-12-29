from elasticsearch import Elasticsearch, helpers
import pandas as pd
from datetime import datetime
import pprint
import pickle
import re

#Connecting to the enron index in ES
es=Elasticsearch('http://enron:spsdata@129.105.88.91:9200')

#Query spec to match anything in a message, i.e. to retrieve all messages
query={"query" : {"match_all" : {}}}

#Count how many messages there are in Enron
count_results=es.search(size=0,index='enron',doc_type='email',body=query) 

count_results 

#Understanding the ingredients
msgs=es.search(index='enron',doc_type='email',body=query)

msgs

#Print keys in msgs
for key in msgs.keys(): print(key)

#Value associated with its key hits
type(msgs['hits']['hits'])

#Pretty Print of email documents for each unique ____id
pprint.pprint(msgs['hits']['hits'][0])


#------------------------------------------------------------------------------

##############----PART 1----#################
query={"query":{"nested":{"path":"headers","query":{"match":{"headers.X-From":"Ken Lay|Kenneth Lay|Ken"}}}}}
es.count(index='enron',doc_type='email',body=query) 
es.search(size=5,index='enron',doc_type='email',body=query)

#------------------------------------------------------------------------------

##############----PART 2----#################
#Create a data frame from the pickled data and standardize the date time format
df_enron_email = pd.read_pickle("eemail_df.pkl")
df_enron_email.fillna("", inplace = True)
df_enron_email['Date'] = pd.to_datetime(df_enron_email.Date, errors='ignore') 
df_enron_email.Date.isnull().sum()
df_enron_email.head(15)

#Unique Email Count - Change Column header
df_enron_email.rename(columns={'X-From': 'XFrom'}, inplace = True)

#Find available options with matching values
df_i = df_enron_email[df_enron_email.From.str.contains('ken|Lay|lay|klay|chairman')]
df_i.rename(columns={'Message-ID': 'MessageID'}, inplace=True)

#Plug viable options into a value list and sort.
value_list = ['ken.skilling@enron.com','chairman.ken@enron.com','kenneth.lay@enron.com','ken.lay-@enron.com','ken.lay-.chairman.of.the.board@enron.com','ken.lay@enron.com','no.address@enron.com',"ken_lay"]
df_2 = df_i[df_i.From.isin(value_list)]
df_2.groupby('From').MessageID.nunique()
df_2


#------------------------------------------------------------------------------

##############----PART 3----#################
#To and From Ken Lay:
query={"query":{"nested":{"path":"headers","query" : {"multi_match" : {"fields" : ["headers.From", "headers.To"],"query":"Ken Lay"}}}}}
es.count(index='enron',doc_type='email',body=query)
es.search(size=5,index='enron',doc_type='email',body=query)

#------ Nothing turned up so we will use the X Fields
query={"query":{"nested":{"path":"headers","query" : {"multi_match" : {"fields" : ["headers.X-From", "headers.X-To"],"query":"Ken Lay"}}}}}
es.count(index='enron',doc_type='email',body=query)
es.search(size=5,index='enron',doc_type='email',body=query)


#------------------------------------------------------------------------------

##############----PART 4----#################

#--Who sent Lay the most emails:
df_temp = df_enron_email
df_temp["Count"] = 1
df_temp = df_temp[(df_enron_email["X-To"].str.contains(".*klay@enron.com*."))]
number_to_klay = df_temp.groupby(["X-From"])["Count"].sum()
number_to_klay = number_to_klay.sort_values(ascending = False)
print("User who sent the most emails to Ken Lay:", number_to_klay.index[0])
print("Number of emails sent by", number_to_klay.index[0], "to Ken Lay:", number_to_klay[0])

#--Who Lay sent the most emails to:
df_temp = df_enron_email
df_temp["Count"] = 1
df_temp = df_temp[(df_enron_email["X-From"].str.contains("Ken Lay"))]
number_to_klay = df_temp.groupby(["X-To"])["Count"].sum()
number_to_klay = number_to_klay.sort_values(ascending = False)
print("User who Ken Lay sent the most emails to:", number_to_klay.index[0])
print("Number of emails sent to", number_to_klay.index[0], "From Ken Lay:", number_to_klay[0])


#------------------------------------------------------------------------------

##############----PART 5----#################

date_min = df_enron_email["Date"].min()
date_max = df_enron_email["Date"].max()

df_temp = df_enron_email
before_bank = df_temp['Date'] <= 'Sat, 1 Dec 2001 24:59:59 -0800 (PST)'
print("Number of emails before bankruptcy:", before_bank.sum())
after_bank = df_temp['Date'] >= 'Sun, 2 Dec 2001 01:00:00 -0800 (PST)'
print("Number of emails after bankruptcy:", after_bank.sum())
#Emails Before: 181,951
#Emails After: 307,944

#------------------------------------------------------------------------------

##############----PART 6----#################
import re
df_temp = df_enron_email[["Subject", "body"]]
arthur_count = df_temp.applymap(lambda x: bool(re.search(".*Arthur Andersen*.", x))).any(axis=1)
print("Number of emails which mention Athur Andersen:", arthur_count.sum())
#885 emails mention Arthur Anderson, Enron's accounting firm.





