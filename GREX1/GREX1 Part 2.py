cd '/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1'

import pandas as pd
import xlrd

######2015 Customer Service File Import#######
CS_2015_Data_df=pd.read_csv('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/sfo_cust_sat_2015_data file_final_WEIGHTED_flysfo.csv')
type(CS_2015_Data_df)
CS_2015_Data_df.shape
CS_2015_Data_df.columns
CS_2015_Data_df.head

######2016 Customer Service File Import#######
CS_2016_Data_df=pd.read_excel('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/2016 SFO Customer Survey Data.xlsx')
type(CS_2016_Data_df)
CS_2016_Data_df.shape
CS_2016_Data_df.columns
CS_2016_Data_df.head

###-----Change 2015 column names-----###
CS_2015_Data_df.rename(columns={'RESPNUM':'RESP_ID',
    'Q19GENDER':'Sex',
    'Q8COM1':'2015_Comment 1',
    'Q8COM2':'2015_Comment 2',
    'Q8COM3':'2015_Comment 3',}, inplace=True)
CS_2015_Data_df.columns

CS_2015_Data_df.Sex.value_counts().head()#Check Distribution of values

#Fix missing values to match other data frame form 2016
CS_2015_Data_df.Sex.replace([1,2,0],['Male','Female','Other'], inplace=True)
CS_2015_Data_df

###-----Create new data frame-----###
CS_2015_Info = CS_2015_Data_df[['Sex','2015_Comment 1','2015_Comment 2',
   '2015_Comment 3']]
CS_2015_Info.head()

CS_2015_C1 = CS_2015_Info[['Sex','2015_Comment 1']].copy()
CS_2015_C2 = CS_2015_Info[['Sex','2015_Comment 2']].copy()
CS_2015_C3 = CS_2015_Info[['Sex','2015_Comment 3']].copy()

CS_2015_C1.rename(columns ={'2015_Comment 1':'Comments'}, inplace=True)
CS_2015_C2.rename(columns ={'2015_Comment 2':'Comments'}, inplace=True)
CS_2015_C3.rename(columns ={'2015_Comment 3':'Comments'}, inplace=True)

CS_2015_C1
CS_2015_C2
CS_2015_C3

CS_2015_Comments_All_df = pd.concat([CS_2015_C1,CS_2015_C2,CS_2015_C3])

#---Final 2015 database---#
CS_2015_Comments_All_df

###-----Change 2016 Column names-----###
CS_2016_Data_df.rename(columns={'*RESPNUM':'RESP_ID',
    'Q20GENDER':'Sex',
    'Q8COM':'2016_Comment 1',
    'Q8COM2':'2016_Comment 2',
    'Q8COM3':'2016_Comment 3',
    'Q8COM4':'2016_Comment 4',
    'Q8COM5':'2016_Comment 5'}, inplace=True)
CS_2016_Data_df
CS_2016_Data_df.columns

###-----Create new data frame-----###
CS_2016_Info = CS_2016_Data_df[['Sex','2016_Comment 1','2016_Comment 2',
   '2016_Comment 3','2016_Comment 4','2016_Comment 5']]
CS_2016_Info.head(20)

CS_2016_Info.Sex.value_counts().head() #Check Distribution of values

CS_2016_C1 = CS_2016_Info[['Sex','2016_Comment 1']].copy()
CS_2016_C2 = CS_2016_Info[['Sex','2016_Comment 2']].copy()
CS_2016_C3 = CS_2016_Info[['Sex','2016_Comment 3']].copy()
CS_2016_C4 = CS_2016_Info[['Sex','2016_Comment 4']].copy()
CS_2016_C5 = CS_2016_Info[['Sex','2016_Comment 5']].copy()

CS_2016_C1.rename(columns ={'2016_Comment 1':'Comments'}, inplace=True)
CS_2016_C2.rename(columns ={'2016_Comment 2':'Comments'}, inplace=True)
CS_2016_C3.rename(columns ={'2016_Comment 3':'Comments'}, inplace=True)
CS_2016_C4.rename(columns ={'2016_Comment 4':'Comments'}, inplace=True)
CS_2016_C5.rename(columns ={'2016_Comment 5':'Comments'}, inplace=True)

CS_2016_C1
CS_2016_C2
CS_2016_C3
CS_2016_C4
CS_2016_C5

CS_2016_Comments_All_df = pd.concat([CS_2016_C1,CS_2016_C2,CS_2016_C3,CS_2016_C4,
    CS_2016_C5])

#---Final 2016 database---#
CS_2016_Comments_All_df

#########------------COMBINING THE DATA----------------#############

CS_2015_Male = CS_2015_Comments_All_df[CS_2015_Comments_All_df.Sex=='Male']
CS_2015_Male.head()

CS_2015_Female = CS_2015_Comments_All_df[CS_2015_Comments_All_df.Sex=='Female']
CS_2015_Female.head()

CS_2016_Male = CS_2016_Comments_All_df[CS_2016_Comments_All_df.Sex=='Male']
CS_2016_Male.head()

CS_2016_Female = CS_2016_Comments_All_df[CS_2016_Comments_All_df.Sex=='Female']
CS_2016_Female.head()

CS_2015_Male.Comments.value_counts().nlargest(3)
CS_2015_Male.Comments.value_counts().head(3)

#Combine both 2015 and 2016 Male/Female data
CS_Comments_All_df = pd.concat([CS_2015_Male,CS_2015_Female,CS_2016_Male,CS_2016_Female])
CS_Comments_All_df

CS_Comments_ser = CS_Comments_All_df.groupby('Sex').Comments.value_counts()
CS_Comments_ser

CS_Comments_ser.groupby(level='Sex',group_keys=False).nlargest(3)
