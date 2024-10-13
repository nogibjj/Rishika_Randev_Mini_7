"""Query the Behaviors data table"""

from databricks import sql
from dotenv import load_dotenv
import os


def query(query_input):
    load_dotenv()
    access_token = os.getenv("databricks")
    server_host = os.getenv("server_host")
    http_path = os.getenv("http_path")
    with sql.connect(server_hostname=server_host,
                     http_path=http_path,
                     access_token=access_token) as conn:
        c = conn.cursor()
        c.execute(query_input)
        print("Query Output: \n")
        print(c.fetchall())
        c.close()
        conn.close()
    return "Success"

     
