import pandas as pd
import sqlite3
from pathlib import Path
import os
import re


def standardize_naming(x):
    output = re.sub('[0-9]+', '', x)
    output = output.strip('-')
    output = output.strip(' ')
    output = output.strip('+')
    
    output = "_".join(output.lower().split(" "))
    return output

## process column names to remove space and add _

def process_columns(col):
    
    col = "_".join(col.lower().split(" "))
                
    return col

## load data in the target directory

def load_data(data_dir, kind = 'company'):

    static = pd.DataFrame()
    tracking = pd.DataFrame()
    general = pd.DataFrame()

    print("loading data......")
    for filename in os.listdir(data_dir):

        if filename.endswith(".csv"):
            print(filename)
            ## renaming
            std_name = standardize_naming(filename)
            os.rename(os.path.join(data_dir, filename), os.path.join(data_dir, std_name))
            df = pd.read_csv(os.path.join(data_dir, std_name))
            
            ## process column names
            df.columns = [process_columns(i) for i in df.columns]
            
            if kind == 'general':
                
                general = general.append(df)
            
            if kind != 'general':
                
                if 'static' in std_name:
                    static = static.append(df)
                if 'tracking' in std_name:
                    tracking = tracking.append(df)
                
    if kind == 'general':
        return general
    else:
        return static, tracking