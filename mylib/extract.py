"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url="https://data.cdc.gov/api/views/hn4x-zwk7/rows.csv?accessType=DOWNLOAD", 
            file_path="data/Behaviors.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



