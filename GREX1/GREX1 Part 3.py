import pandas as pd
import xlrd

######2015 Customer Service File Import#######
CS_2015_Data_Live=pd.read_csv('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/sfo_cust_sat_2015_data file_final_WEIGHTED_flysfo.csv')
type(CS_2015_Data_df)
CS_2015_Data_Live.shape
CS_2015_Data_Live.columns
CS_2015_Data_Live.head

######2016 Customer Service File Import#######
CS_2016_Data_Live=pd.read_excel('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/2016 SFO Customer Survey Data.xlsx')
type(CS_2016_Data_df)
CS_2016_Data_Live.shape
CS_2016_Data_Live.columns
CS_2016_Data_Live.head

###-----Change 2015 column names-----###
CS_2015_Data_Live.rename(columns={'RESPNUM':'RESP_ID',
    'Q19GENDER':'Sex',
    'Q7ALL':'All_Comments','Q16LIVE':'Live_In'}, inplace=True)
CS_2015_Data_Live.columns

CS_2015_Data_Live.Live_In.value_counts().head()#Check Distribution of values

#Fix values to match other data frame form 2016
CS_2015_Data_Live.Live_In.replace([1,2,3,0],['County Bay Area','Northern California Outside Bay Area','In Another Region','Blank'], inplace=True)
CS_2015_Data_Live

###-----Create new data frame-----###
CS_2015_Live_Info = CS_2015_Data_Live[['Live_In','All_Comments']]
CS_2015_Live_Info.head()

###-----Change 2016 Column names-----###
CS_2016_Data_Live.rename(columns={'*RESPNUM':'RESP_ID',
    'Q20GENDER':'Sex',
    'Q7ALL':'All_Comments','Q16LIVE':'Live_In'}, inplace=True)
CS_2016_Data_Live
CS_2016_Data_Live.columns

#Fix missing values to match other data frame form 2015
CS_2016_Data_Live.Live_In.replace([1,2,3,0],['County Bay Area','Northern California Outside Bay Area','In Another Region','Blank'], inplace=True)
CS_2016_Data_Live

###-----Create new data frame-----###
CS_2016_Live_Info = CS_2016_Data_Live[['Live_In','All_Comments']]
CS_2016_Live_Info.head(20)

CS_2016_Live_Info.Live_In.value_counts().head() #Check Distribution of values

#########------------COMBINING THE DATA----------------#############
#Combine both 2015 and 2016 data
CS_All_Comments_df = pd.concat([CS_2016_Live_Info,CS_2015_Live_Info])
CS_All_Comments_df

CS_All_Comments_ser = CS_All_Comments_df.groupby('Live_In').All_Comments.value_counts()
CS_All_Comments_ser

CS_All_Comments_ser.groupby(level='Live_In',group_keys=False).nlargest(3)
