"""
Test goes here

"""

from mylib.extract import extract
#from mylib.transform_load import load
from mylib.query import query
from databricks import sql
from dotenv import load_dotenv
import os


def test_extract():
    extracted_data = extract()
    assert extracted_data == "data/MH.csv"


def test_transform_load():
        load_dotenv()
        access_token = os.getenv("databricks")
        server_host = os.getenv("server_host")
        http_path = os.getenv("http_path")
        with sql.connect(server_hostname=server_host,
                     http_path=http_path,
                     access_token=access_token) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM rr368_MentalHealth LIMIT 4")
            result = c.fetchall()
            assert result is not None
            c.close()
        conn.close()


def test_query():
    input = "WITH t1 AS (SELECT Indicator, MAX(Value) Max_Value_Across_States \
        FROM default.rr368_mentalhealth \
        GROUP BY Indicator) \
        SELECT t2.State, t2.Indicator, t2.Value, \
        t1.Max_Value_Across_States, \
        RANK() OVER(PARTITION BY t2.Indicator ORDER BY t2.Value DESC) Value_Rank \
        FROM default.rr368_mentalhealth AS t2 \
        JOIN t1 \
        ON (t1.Indicator = t2.Indicator) \
        LIMIT 1"
    results = query(input)
    assert results == "Success"


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_query()
