import pandas as pd
import xlrd

######2015 Customer Service File Import#######
CS_2015_Data_df=pd.read_csv('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/sfo_cust_sat_2015_data file_final_WEIGHTED_flysfo.csv')
type(CS_2015_Data_df)
CS_2015_Data_df.shape
CS_2015_Data_df.columns
CS_2015_Data_df.head

######2016 Customer Service File Import#######
CS_2016_xlfile=pd.ExcelFile('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/2016 SFO Customer Survey Data.xlsx')
CS_2016_xlfile.sheet_names

CS_2016_Data_df=pd.read_excel('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/2016 SFO Customer Survey Data.xlsx')
type(CS_2016_Data_df)
CS_2016_Data_df.shape
CS_2016_Data_df.columns
CS_2016_Data_df.dtypes
CS_2016_Data_df.head() #displays the first amount of rows specified. If blank, it does 5
CS_2016_Data_df.tail(3)#displays the last amount of rows specified. If blank, it does 5

######2014 Customer Service File Import#######
CS_2014_xlfile=pd.ExcelFile('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/sfo cust sat 2014 data file_WEIGHTED_flysfo.xlsx')
CS_2014_xlfile.sheet_names

CS_2014_Data_df=pd.read_excel('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/sfo cust sat 2014 data file_WEIGHTED_flysfo.xlsx')
type(CS_2014_Data_df)
CS_2014_Data_df.shape
CS_2014_Data_df.columns
CS_2014_Data_df.dtypes
CS_2014_Data_df.head() #displays the first amount of rows specified. If blank, it does 5
CS_2014_Data_df.tail(3)#displays the last amount of rows specified. If blank, it does 5

#Modify Important Column Names 2014
CS_2014_Data_df.rename(columns={'RESPNUM':'RESP_ID','DESTGEO':'REGION','Q7ART':'RATE_GEN_ART',
   'Q7FOOD':'RATE_GEN_FOOD','Q7STORE':'RATE_GEN_STORE','Q7SIGN':'RATE_GEN_SIGN',
   'Q7WALKWAYS':'RATE_GEN_WALKWAYS','Q7SCREENS':'RATE_GEN_SCREENS',
   'Q7INFODOWN':'RATE_GEN_INFODOWN','Q7INFOUP':'RATE_GEN_INFOUP','Q7WIFI':'RATE_GEN_WIFI',
   'Q7ROADS':'RATE_GEN_ROADS','Q7PARK':'RATE_GEN_PARK','Q7AIRTRAIN':'RATE_GEN_AIRTRAIN',
   'Q7LTPARKING':'RATE_GEN_LTPARK','Q7RENTAL':'RATE_GEN_RENTAL','Q7ALL':'RATE_GEN_ALL',
   'Q9BOARDING':'RATE_CLEAN_BOARDING','Q9AIRTRAIN':'RATE_CLEAN_AIRTRAIN',
   'Q9RENTAL':'RATE_CLEAN_RENTAL','Q9FOOD':'RATE_CLEAN_FOOD','Q9RESTROOM':'RATE_CLEAN_RESTROOM',
   'Q9ALL':'RATE_CLEAN_ALL','Q10SAFE':'RATE_SAFETY','Q12PRECHECKRATE':'RATE_PRECHK',
   'Q13GETRATE':'RATE_GETEXP','Q14FIND':'RATE_FIND_WAY','Q14PASSTHRU':'RATE_PASS_TSA'}, inplace=True)

#Modify Important Column Names 2015
CS_2015_Data_df.rename(columns={'RESPNUM':'RESP_ID',
    'DESTGEO':'REGION',
    'Q7ART':'RATE_GEN_ART',
    'Q7FOOD':'RATE_GEN_FOOD',
    'Q7STORE':'RATE_GEN_STORE',
    'Q7SIGN':'RATE_GEN_SIGN',
    'Q7WALKWAYS':'RATE_GEN_WALKWAYS',
    'Q7SCREENS':'RATE_GEN_SCREENS',
    'Q7INFODOWN':'RATE_GEN_INFODOWN',
    'Q7INFOUP':'RATE_GEN_INFOUP',
    'Q7WIFI':'RATE_GEN_WIFI',
    'Q7ROADS':'RATE_GEN_ROADS',
    'Q7PARK':'RATE_GEN_PARK',
    'Q7AIRTRAIN':'RATE_GEN_AIRTRAIN',
    'Q7LTPARKING':'RATE_GEN_LTPARK',
    'Q7RENTAL':'RATE_GEN_RENTAL',
    'Q7ALL':'RATE_GEN_ALL',
    'Q9BOARDING':'RATE_CLEAN_BOARDING',
    'Q9AIRTRAIN':'RATE_CLEAN_AIRTRAIN',
    'Q9RENTAL':'RATE_CLEAN_RENTAL',
    'Q9FOOD':'RATE_CLEAN_FOOD',
    'Q9RESTROOM':'RATE_CLEAN_RESTROOM',
    'Q9ALL':'RATE_CLEAN_ALL',
    'Q10SAFE':'RATE_SAFETY',
    'Q12PRECHEKCRATE':'RATE_PRECHK',
    'Q13GETRATE':'RATE_GETEXP',
    'Q14FIND':'RATE_FIND_WAY',
    'Q14PASSTHRU':'RATE_PASS_TSA'}, inplace=True)

#Modify Important Column Names 2016
CS_2016_Data_df.rename(columns={'*RESPNUM':'RESP_ID','DESTGEO':'REGION','Q7ART':'RATE_GEN_ART',
   'Q7FOOD':'RATE_GEN_FOOD','Q7STORE':'RATE_GEN_STORE','Q7SIGN':'RATE_GEN_SIGN',
   'Q7WALKWAYS':'RATE_GEN_WALKWAYS','Q7SCREENS':'RATE_GEN_SCREENS',
   'Q7INFODOWN':'RATE_GEN_INFODOWN','Q7INFOUP':'RATE_GEN_INFOUP','Q7WIFI':'RATE_GEN_WIFI',
   'Q7ROADS':'RATE_GEN_ROADS','Q7PARK':'RATE_GEN_PARK','Q7AIRTRAIN':'RATE_GEN_AIRTRAIN',
   'Q7LTPARKING':'RATE_GEN_LTPARK','Q7RENTAL':'RATE_GEN_RENTAL','Q7ALL':'RATE_GEN_ALL',
   'Q9BOARDING':'RATE_CLEAN_BOARDING','Q9AIRTRAIN':'RATE_CLEAN_AIRTRAIN',
   'Q9RENTAL':'RATE_CLEAN_RENTAL','Q9FOOD':'RATE_CLEAN_FOOD','Q9RESTROOM':'RATE_CLEAN_RESTROOM',
   'Q9ALL':'RATE_CLEAN_ALL','Q10SAFE':'RATE_SAFETY','Q12PRECHECKRATE':'RATE_PRECHK',
   'Q13GETRATE':'RATE_GETEXP','Q14FIND':'RATE_FIND_WAY','Q14PASSTHRU':'RATE_PASS_TSA'}, inplace=True)

#Double Checking Columns
CS_2014_Data_df.columns
CS_2015_Data_df.columns
CS_2016_Data_df.columns

#Adding the Year Columns
#Add 2014
CS_2014_Data_df = CS_2014_Data_df.assign(YEAR=2014)
CS_2014_Data_df.columns
CS_2014_Data_df.head(6)

#Add 2015
CS_2015_Data_df = CS_2015_Data_df.assign(YEAR=2015)
CS_2015_Data_df.columns
CS_2015_Data_df.head(6)

#Add 2016
CS_2016_Data_df = CS_2016_Data_df.assign(YEAR=2016)
CS_2016_Data_df.columns
CS_2016_Data_df.head(6)

#######---------------MANIPULATING 2014 DATA----------------------#############

#Selecting Specific columns
CS_2014_Data_INFO = CS_2014_Data_df[['RESP_ID','REGION','RATE_GEN_ART',
   'RATE_GEN_FOOD','RATE_GEN_STORE','RATE_GEN_SIGN','RATE_GEN_WALKWAYS',
   'RATE_GEN_SCREENS','RATE_GEN_INFODOWN','RATE_GEN_INFOUP','RATE_GEN_WIFI',
   'RATE_GEN_ROADS','RATE_GEN_PARK','RATE_GEN_AIRTRAIN','RATE_GEN_LTPARK',
   'RATE_GEN_RENTAL','RATE_GEN_ALL','RATE_CLEAN_BOARDING','RATE_CLEAN_AIRTRAIN',
   'RATE_CLEAN_RENTAL','RATE_CLEAN_FOOD','RATE_CLEAN_RESTROOM','RATE_CLEAN_ALL',
   'RATE_SAFETY','RATE_PRECHK','RATE_GETEXP','RATE_FIND_WAY','RATE_PASS_TSA','YEAR']]
CS_2014_Data_INFO.head()

#Check for right amount of records
CS_2014_Data_INFO.shape

#Check for every unique ID (2818)
CS_2014_Data_INFO.RESP_ID.nunique()

#See if there are any nan values (RATE_PRECHK has nan values)
CS_2014_Data_INFO.notnull().sum()

#Check RATE_PRECHK
CS_2014_Data_INFO.RATE_PRECHK.head(6)

#Distribution of values
CS_2014_Data_INFO.RATE_PRECHK.value_counts().head()

(CS_2014_Data_INFO.RATE_PRECHK==nan).sum()

CS_2014_Data_INFO.RATE_PRECHK.value_counts(dropna=False).head()

#Apply value counts to the subset of columns
CS_2014_Data_df[['RATE_PRECHK']].apply(pd.value_counts)


#######---------------MANIPULATING 2015 DATA----------------------#############

#Selecting Specific columns
CS_2015_Data_INFO = CS_2015_Data_df[['RESP_ID','REGION','RATE_GEN_ART',
   'RATE_GEN_FOOD','RATE_GEN_STORE','RATE_GEN_SIGN','RATE_GEN_WALKWAYS',
   'RATE_GEN_SCREENS','RATE_GEN_INFODOWN','RATE_GEN_INFOUP','RATE_GEN_WIFI',
   'RATE_GEN_ROADS','RATE_GEN_PARK','RATE_GEN_AIRTRAIN','RATE_GEN_LTPARK',
   'RATE_GEN_RENTAL','RATE_GEN_ALL','RATE_CLEAN_BOARDING','RATE_CLEAN_AIRTRAIN',
   'RATE_CLEAN_RENTAL','RATE_CLEAN_FOOD','RATE_CLEAN_RESTROOM','RATE_CLEAN_ALL',
   'RATE_SAFETY','RATE_PRECHK','RATE_GETEXP','RATE_FIND_WAY','RATE_PASS_TSA','YEAR']]
CS_2015_Data_INFO.head()

#Check for right amount of records
CS_2015_Data_INFO.shape

#Check for every unique ID (2598)
CS_2015_Data_INFO.RESP_ID.nunique()

#See if there are any nan values (There are no nan values)
CS_2015_Data_INFO.notnull().sum()


#######---------------MANIPULATING 2016 DATA----------------------#############

#Selecting Specific columns
CS_2016_Data_INFO = CS_2016_Data_df[['RESP_ID','REGION','RATE_GEN_ART',
   'RATE_GEN_FOOD','RATE_GEN_STORE','RATE_GEN_SIGN','RATE_GEN_WALKWAYS',
   'RATE_GEN_SCREENS','RATE_GEN_INFODOWN','RATE_GEN_INFOUP','RATE_GEN_WIFI',
   'RATE_GEN_ROADS','RATE_GEN_PARK','RATE_GEN_AIRTRAIN','RATE_GEN_LTPARK',
   'RATE_GEN_RENTAL','RATE_GEN_ALL','RATE_CLEAN_BOARDING','RATE_CLEAN_AIRTRAIN',
   'RATE_CLEAN_RENTAL','RATE_CLEAN_FOOD','RATE_CLEAN_RESTROOM','RATE_CLEAN_ALL',
   'RATE_SAFETY','RATE_PRECHK','RATE_GETEXP','RATE_FIND_WAY','RATE_PASS_TSA','YEAR']]
CS_2014_Data_INFO.head()

#Check for right amount of records
CS_2016_Data_INFO.shape

#Check for every unique ID (3087)
CS_2016_Data_INFO.RESP_ID.nunique()

#See if there are any nan values (There are no nan values)
CS_2016_Data_INFO.notnull().sum()

#Check RATE_PRECHK
CS_2016_Data_INFO.RATE_PRECHK.head(6)

#Distribution of values
CS_2016_Data_INFO.RATE_PRECHK.value_counts().head()

(CS_2016_Data_INFO.RATE_PRECHK==' ').sum()

CS_2016_Data_INFO.RATE_PRECHK.value_counts(dropna=False).head()

#Apply value counts to the subset of columns
CS_2016_Data_df[['RATE_PRECHK']].apply(pd.value_counts)


###---Concatentate the databases---###

CS_Data_df = pd.concat([CS_2014_Data_INFO, CS_2016_Data_INFO, CS_2015_Data_INFO])

CS_Data_df.shape
CS_Data_df.columns
CS_Data_df.head()


CS_Data_df.to_csv("CS_ALL_DATA.csv",index=False)
ls

