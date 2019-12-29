import pandas as pd
import xlrd
import sqlalchemy

#Part 1 A)
#Import the CSV files into Pandas dataframe

cust_df=pd.read_csv('jpf6752_customer.csv')
type(cust_df)
cust_df.shape
cust_df.columns
cust_df.head(4)

cust_df.insert(9,'active_buyer', np.where(cust_df.buyer_status=='ACTIVE',1,2))
cust_df.head(10)

cust_df2 = cust_df.loc[cust_df['buyer_status'] == 'ACTIVE']
cust_df2.head(10)

item_df=pd.read_csv('jpf6752_item.csv')
type(item_df)
item_df.shape
item_df.columns
item_df.head(4)

mail_df=pd.read_csv('jpf6752_mail.csv')
type(cust_df)
mail_df.shape
mail_df.columns
mail_df.head(4)


#-------Part 2--------#
#Witing the tables to a sql data frame 
import sqlalchemy #installed package SQLAlchemy 1.1.6-1
from sqlalchemy import create_engine

engine=create_engine('sqlite:///xyz.db')
conn=engine.connect()

engine.table_names()

cust_df.to_sql('Customers',conn,index=False)

count = pd.read_sql_query("SELECT COUNT(*) FROM Customers",conn)
print(count)

cust_df2=pd.read_sql('Customers',conn)
cust_df2.head()

item_df.to_sql('Items',conn,index=False)
mail_df.to_sql('Mail',conn,index=False)

engine.table_names()


#-------Part 3--------#
#PART A
catsum2 = cust_df
catsum2.head(20)

catsum3 = catsum2[catsum2.buyer_status == 'ACTIVE']
catsum3.head()

catsum4 = catsum3.groupby('acctno')['ytd_sales_2009'].sum().reset_index()
print catsum4

catsum4['heavy_buyer'] = np.where(catsum4['ytd_sales_2009'] >= (catsum4['ytd_sales_2009'].quantile(0.9)), 'Y','N')

catsum4.head(20)

#PART B-F

#Creating Second data set
cc_info = cust_df2[['acctno','amex_reg','amex_prem','disc_reg','disc_prem','visa_reg','visa_prem','mc_reg','mc_prem','med_inc','adult1_g','adult2_g','zip','zip4']]
cc_info.head()

custsum = pd.merge(catsum4, cc_info, on='acctno')
custsum.head()

custsum['amex_reg'] = np.where(custsum['amex_reg'] == 'Y', 'Y','N')
custsum['amex_prem'] = np.where(custsum['amex_prem'] == 'Y', 'Y','N')
custsum['disc_reg'] = np.where(custsum['disc_reg'] == 'Y', 'Y','N')
custsum['visa_reg'] = np.where(custsum['visa_reg'] == 'Y', 'Y','N')
custsum['visa_prem'] = np.where(custsum['visa_prem'] == 'Y', 'Y','N')
custsum['mc_reg'] = np.where(custsum['mc_reg'] == 'Y', 'Y','N')
custsum['mc_prem'] = np.where(custsum['mc_prem'] == 'Y', 'Y','N')

print custsum

#Part G

custsum.to_sql('Customer_Summary',conn,index=False)
engine.table_names()

#------Part 4------#
#PART A
#First Merge DB#
a_cust = pd.DataFrame(cust_df.groupby('acctno').buyer_status.unique()).reset_index()
a_cust.head(20)

item2_df = item_df
item2_df.head()

c_item = pd.DataFrame(item2_df.groupby('acctno').deptdescr.value_counts())
c_item.head()

cd_item = pd.DataFrame(c_item.unstack(level=-1, fill_value='N')).reset_index()
cd_item.head()

#Second Merge DB#
b_item = pd.DataFrame(item_df.groupby('acctno').totamt.sum()).reset_index()
b_item.head()

#First Merge#
d_item = pd.merge(cd_item, a_cust, left_on='acctno',right_on='acctno')
d_item.head()

#Second Merge#
f_item = pd.merge(d_item, b_item, left_on='acctno',right_on='acctno')

cust_item = f_item[(f_item.buyer_status=='ACTIVE')]

pd.DataFrame(cust_item)

#Writing to csv#
cust_item.to_csv("Customer_Item_Detail.csv",index=False)

#Writing to xyz database
cust_item.to_sql('Customer_Item_Detail',conn,index=False)
engine.table_names()

#-----Part 5-----#
freq_p = cust_df2.merge(item_df)
freq_p.head()

freq_p2 = freq_p[['acctno','adult1_g','totamt','qty','deptdescr']]
freq_p2.head()

#Part 1 of Part 5
check2 = freq_p2.groupby('adult1_g').adult1_g.count()
check2

#Part 2 of Part 5
check3 = freq_p2.groupby('deptdescr').deptdescr.value_counts()
check3

freq_p2.groupby(by=['adult1_g','deptdescr'])['qty','totamt'].sum()

#Part 2B of Part 5
check = freq_p2.groupby('adult1_g').deptdescr.value_counts()
check
check.groupby(level='adult1_g',group_keys=False).nlargest(6)




























