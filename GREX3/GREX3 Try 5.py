import json
import os
import pandas as pd
from pandas.io.json import json_normalize

file_list = os.listdir('.') 
file_list

with open("100506.json") as input_file:
    jsondat = json.load(input_file)
    reviews = json_normalize(jsondat)
    hotel_info = jsondat['HotelInfo']
    reviews_df = json_normalize(reviews)
    hotels_df = json_normalize(hotel_info)
    reviews_df['HotelID'] = hotels_df.iloc[0]['HotelID']
    df = pd.DataFrame(reviews_df)
    
    df
        
