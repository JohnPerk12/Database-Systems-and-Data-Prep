import pandas as pd
import xlrd

######Customer Select File Import#######
CS_Select_Data_df=pd.read_csv('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/select_resps.csv')
type(CS_Select_Data_df)
CS_Select_Data_df
CS_Select_Data_df.shape
CS_Select_Data_df.columns
CS_Select_Data_df.head

######2015 Customer Service File Import#######
CS_2015_Sel_Data_df=pd.read_csv('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/sfo_cust_sat_2015_data file_final_WEIGHTED_flysfo.csv')
type(CS_2015_Sel_Data_df)
CS_2015_Sel_Data_df.shape
CS_2015_Sel_Data_df.columns
CS_2015_Sel_Data_df.head

######2016 Customer Service File Import#######
CS_2016_Sel_Data_df=pd.read_excel('/Users/johnperkins/Dropbox (Personal)/Northwestern/5. Fall 2017/PREDICT 420/Assignment 1/2016 SFO Customer Survey Data.xlsx')
type(CS_2016_Sel_Data_df)
CS_2016_Sel_Data_df.shape
CS_2016_Sel_Data_df.columns
CS_2016_Sel_Data_df.head

###-----Change Select Customer column names-----###
CS_Select_Data_df.rename(columns={'RESPNUM':'RESP_ID',
    'year':'Year',}, inplace=True)
CS_Select_Data_df.columns

###-----Change 2015 column names-----###
#This was performed to help with working with the columns. These names are easier
#to understand
CS_2015_Sel_Data_df.rename(columns={'RESPNUM':'RESP_ID',
    'INTDATE':'Date_of_Interview','Q5TIMESFLOWN':'Times_Flown_SFO','Q6LONGUSE':'How_Long_Using_SFO','Q3PARK':'Parking'}, inplace=True)
CS_2015_Sel_Data_df.columns

#Fix values to match other data frame form 2016
CS_2015_Sel_Data_df.Date_of_Interview.replace([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],['2015-05-01 00:00:00',
    '2015-05-02 00:00:00','2015-05-03 00:00:00','2015-05-04 00:00:00','2015-05-05 00:00:00',
    '2015-05-06 00:00:00','2015-05-07 00:00:00','2015-05-08 00:00:00','2015-05-09 00:00:00',
    '2015-05-10 00:00:00','2015-05-11 00:00:00','2015-05-12 00:00:00','2015-05-13 00:00:00',
    '2015-05-14 00:00:00','2015-05-15 00:00:00','2015-05-16 00:00:00','2015-05-17 00:00:00',
    '2015-05-18 00:00:00','2015-05-19 00:00:00','2015-05-20 00:00:00','2015-05-21 00:00:00',
    '2015-05-22 00:00:00','2015-05-23 00:00:00','2015-05-24 00:00:00','2015-05-25 00:00:00',
    '2015-05-26 00:00:00','2015-05-27 00:00:00','2015-05-28 00:00:00','2015-05-29 00:00:00',
    '2015-05-30 00:00:00','2015-05-31 00:00:00'], inplace=True)
CS_2015_Sel_Data_df

CS_2015_Sel_Data_df.Times_Flown_SFO.replace([1,2,3,4,5,6,0],['1 Time','2 Times','3-6 Times','7-12 Times','13-24 Times','More than 24','Blank'], inplace=True)
CS_2015_Sel_Data_df

CS_2015_Sel_Data_df.How_Long_Using_SFO.replace([1,2,3,4,0],['Less than 1 Year','1-5 Years','6-10 Years','10+ Years','Blank'], inplace=True)
CS_2015_Sel_Data_df

CS_2015_Sel_Data_df.Parking.replace([1,2,3,4,0],['Domestic (Garage)','International Garage','SFO Long Term','Off-Airport','Blank'], inplace=True)
CS_2015_Sel_Data_df

###-----Create new data frame-----###
CS_2015_Sel_Info = CS_2015_Sel_Data_df[['RESP_ID','Date_of_Interview','Times_Flown_SFO','How_Long_Using_SFO','Parking']]
CS_2015_Sel_Info.head()


###-----Change 2016 Column names-----###
CS_2016_Sel_Data_df.rename(columns={'*RESPNUM':'RESP_ID','INTDATE':'Date_of_Interview',
    'Q5TIMESFLOWN':'Times_Flown_SFO',
    'Q6LONGUSE':'How_Long_Using_SFO',
    'Q3PARK':'Parking'}, inplace=True)
CS_2016_Sel_Data_df.columns
CS_2016_Sel_Data_df

#Fix missing values to match other data frame form 2016
CS_2016_Sel_Data_df.Times_Flown_SFO.replace([1,2,3,4,5,6,0],['1 Time','2 Times','3-6 Times','7-12 Times','13-24 Times','More than 24','Blank'], inplace=True)
CS_2016_Sel_Data_df

CS_2016_Sel_Data_df.How_Long_Using_SFO.replace([1,2,3,4,0],['Less than 1 Year','1-5 Years','6-10 Years','10+ Years','Blank'], inplace=True)
CS_2016_Sel_Data_df

CS_2016_Sel_Data_df.Parking.replace([1,2,3,4,0],['Domestic (Garage)','International Garage','SFO Long Term','Off-Airport','Blank'], inplace=True)
CS_2016_Sel_Data_df

###-----Create new data frame-----###
CS_2016_Sel_Info = CS_2016_Sel_Data_df[['RESP_ID','Date_of_Interview','Times_Flown_SFO','How_Long_Using_SFO','Parking']]
CS_2016_Sel_Info.head()

CS_Sel_All_df = pd.concat([CS_2015_Sel_Info,CS_2016_Sel_Info])
CS_Sel_All_df

###-----Create New Data Frame for Parking-----###
CS_2016_Sel_Park = CS_Sel_All_df[['RESP_ID','Parking']]
CS_2016_Sel_Park.head()

#Place all of the select passengers into a list for part c)
CS_Select_List = CS_Select_Data_df.RESP_ID.tolist()
CS_Select_List

CS_2016_Sel_Park.RESP_ID.isin(CS_Select_List).head()

CS_Select_Data_PARKFin = CS_2016_Sel_Park[CS_2016_Sel_Park.RESP_ID.isin(CS_Select_List)]
CS_Select_Data_PARKFin

CS_Select_Data_PARKFin.sort_values(by='RESP_ID')

CS_All_Parking = CS_Select_Data_PARKFin.groupby('Parking').RESP_ID.value_counts()
CS_All_Parking

###-----Create New Data Frame for Times Flown-----###
CS_2016_Sel_Times = CS_Sel_All_df[['RESP_ID','Times_Flown_SFO']]
CS_2016_Sel_Times.head()


#Place all of the select passengers into a list for part c)
CS_Select_List = CS_Select_Data_df.RESP_ID.tolist()
CS_Select_List

CS_2016_Sel_Times.RESP_ID.isin(CS_Select_List).head()

CS_Select_Data_TimesFin = CS_2016_Sel_Times[CS_2016_Sel_Times.RESP_ID.isin(CS_Select_List)]
CS_Select_Data_TimesFin

CS_Select_Data_TimesFin.sort_values(by='RESP_ID')

CS_All_Times = CS_Select_Data_TimesFin.groupby('Times_Flown_SFO').RESP_ID.value_counts()
CS_All_Times

###-----Create New Data Frame for How Long Using SFO-----###
CS_2016_Sel_Long = CS_Sel_All_df[['RESP_ID','How_Long_Using_SFO']]
CS_2016_Sel_Long.head()

#Place all of the select passengers into a list for part c)
CS_Select_List = CS_Select_Data_df.RESP_ID.tolist()
CS_Select_List

CS_2016_Sel_Long.RESP_ID.isin(CS_Select_List).head()

CS_Select_Data_LongFin = CS_2016_Sel_Long[CS_2016_Sel_Long.RESP_ID.isin(CS_Select_List)]
CS_Select_Data_LongFin

CS_Select_Data_LongFin.sort_values(by='RESP_ID')

CS_All_Long = CS_Select_Data_LongFin.groupby('How_Long_Using_SFO').RESP_ID.value_counts()
CS_All_Long

#Frequency table for all variables
CS_All_Parking.groupby(level='Parking',group_keys=False).nlargest(3)
CS_All_Times.groupby(level='Times_Flown_SFO',group_keys=False).nlargest(3)
CS_All_Long.groupby(level='How_Long_Using_SFO',group_keys=False).nlargest(3)







