import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from scipy.stats import norm
from scipy import stats
import os
import glob
import math
from geopy.distance import geodesic

        
class DataProcessor:
    def read_text_files(self, directory):
        abs_directory = os.path.abspath(directory)
        file_contents = []
        txt_files = glob.glob(os.path.join(abs_directory, "*.txt"))
        for file_path in txt_files:
            with open(file_path, "r") as file:
                content = file.read()
                file_contents.append(content)
        return file_contents

    def list_to_dataframe(self, data_list):
        data_string = ' '.join(data_list)
        lines = data_string.split("\n")
        data = [line.split() for line in lines]
        df = pd.DataFrame(data)
        return df
    
    def manipulate_data(self, df):
        new_column_names={0: 'latitude', 1: 'longtitude', 2: 'occupancy',3:'time'}
        df_copy = df.copy(deep=False) #copy dataframe without saving memory
        df_copy = df_copy.rename(columns=new_column_names)
        df_copy['time'] = pd.to_datetime(df_copy['time'],unit='s')
        df_copy['year'] = df_copy['time'].dt.year
        df_copy['month'] = df_copy['time'].dt.month
        df_copy['day'] = df_copy['time'].dt.day
        df_copy['hour'] = df_copy['time'].dt.hour
        df_copy['minute'] = df_copy['time'].dt.minute
        df_copy['second'] = df_copy['time'].dt.second
        return df_copy
    
    def clear_data(self, data):
        data.dropna(inplace=True)
        data.drop_duplicates()
        #data['latitude'] = data['latitude'].astype("float")
        #data['longtitude'] = data['longtitude'].astype("float")
        #data['occupancy'] = data['occupancy'].astype("float")
        return data
    
    
    

