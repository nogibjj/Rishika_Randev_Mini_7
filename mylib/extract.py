"""
Extract certain columns and the first 100 rows of a 
dataset from a data.gov URL 
regarding health behaviors (nutrition, physical activity, and diet)
across the U.S.
"""
import requests
import pandas as pd
import os

def extract(url="https://data.cdc.gov/api/views/8pt5-q6wp/rows.csv?accessType=DOWNLOAD", 
            file_path="data/MH.csv", directory = "data"):
    """"Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    df = pd.read_csv(file_path)
    df_subset = df.loc[(df["Group"] == "By State") \
        & (df["Time Period Start Date"] == "05/07/2020"), \
        ["Indicator", "Group", "State", "Time Period Start Date", \
        "Time Period End Date", "Value", "High CI"]]
    df_subset.to_csv(file_path, index=False)
    print("Successfully extracted data")   
    return file_path



