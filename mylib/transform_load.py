"""
Transforms and Loads data into a Databricks database
"""

import csv
import os
from databricks import sql
from dotenv import load_dotenv


# load the csv file and insert into Databricks db
def load(dataset="data/MH.csv"):
    """ "Transforms and Loads data into Databricks"""

    # prints the full working directory and path
    print(f"Locating dataset at: {os.getcwd()}/{dataset}")
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)
    load_dotenv()
    access_token = os.getenv("databricks")
    server_host = os.getenv("server_host")
    http_path = os.getenv("http_path")
    with sql.connect(server_hostname=server_host,
                     http_path=http_path,
                     access_token=access_token) as conn:
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS rr368_MentalHealth")
        c.execute("CREATE TABLE IF NOT EXISTS rr368_MentalHealth \
        (Indicator string, Group string, State string, Time_Period_Start_Date string, Time_Period_End_Date string, Value float, High_CI float)") 
    # insert
        c.executemany(
        "INSERT INTO rr368_MentalHealth (Indicator, Group, State, \
        Time_Period_Start_Date, Time_Period_End_Date, Value, High_CI) VALUES (?, ?, ?, ?, ?, try_cast(? as float), try_cast(? as float))", 
        payload,)
        c.close()
    print("Successfully transformed and loaded data to Databricks")
    return "Success"
