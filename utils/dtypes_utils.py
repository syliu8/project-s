import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path
from sqlalchemy import create_engine


def convert_to_int(x):
    try:
        y =  int(x)
        return y
        
    except:
        return np.NaN

def convert_to_float(x):
    try:
        y =  float(x)
        return y
        
    except:
        return np.NaN
    
    
def convert_to_string(x):
    try:
        y =  str(x)
        return y
        
    except:
        ### TODO: need to decide whether we should use nan
        ### Pro: easy to filter nulls in the df by isna()
        return np.NaN
    
def convert_to_boolean(x):
    try:
        y =  bool(x)
        return y
        
    except:
        return np.NaN
    
def convert_to_timestamp(x):
    try:
        y = pd.to_datetime(x)
        return y
    except:
        ### TODO: need to decide whether we should use nan
        ### Pro: easy to filter nulls in the df by isna()
        return np.NaN
    

def dtypes_wrapper(df, dtype_df):
    
    processed_df = df.copy()
    
    for col in df.columns:
        col_type = dtype_df.loc[dtype_df['name']==col, 'type'].values[0]
        
        if col_type == 'int':
            processed_df[col] = processed_df[col].apply(lambda x: convert_to_int(x))
            
        elif col_type == 'float':
            processed_df[col] = processed_df[col].apply(lambda x: convert_to_float(x))
            
        elif col_type == 'varchar' or col_type == 'varchar(32)' or col_type == 'text':
            processed_df[col] = processed_df[col].apply(lambda x: convert_to_string(x))
            
        elif col_type == 'BOOLEAN':
            processed_df[col] = processed_df[col].apply(lambda x: convert_to_boolean(x))

    return processed_df