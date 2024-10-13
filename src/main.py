"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
import fire


def etl():
    extract()
    load()


def complex_query(input=None):
    if input is None:
        input = "WITH t1 AS (SELECT Indicator, MAX(Value) Max_Value_Across_States \
        FROM default.rr368_mentalhealth \
        GROUP BY Indicator) \
        SELECT t2.State, t2.Indicator, t2.Value, \
        t1.Max_Value_Across_States, \
        RANK() OVER(PARTITION BY t2.Indicator ORDER BY t2.Value DESC) Value_Rank \
        FROM default.rr368_mentalhealth AS t2 \
        JOIN t1 \
        ON (t1.Indicator = t2.Indicator) \
        LIMIT 3"
    query(input)


if __name__ == "__main__":
    fire.Fire()
