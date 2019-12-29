import json
import os
import pandas as pd
from pandas.io.json import json_normalize

file_list = os.listdir('.') 
file_list

company_list=[]
for file in file_list:
    with open(file) as input_file:
        jsondat = json.load(input_file)
        reviews = jsondat['Reviews']
        hotel_info = jsondat['HotelInfo']
        reviews_df = json_normalize(reviews)
        hotels_df = json_normalize(hotel_info)
        reviews_df['HotelID'] = hotels_df.iloc[0]['HotelID']
        df = pd.DataFrame(reviews_df)
        company_list.append(df)
company_list

reviews_final = pd.concat(company_list)

reviews_final.shape