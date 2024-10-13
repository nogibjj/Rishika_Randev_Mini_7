"""
Test goes here

"""

from src.mylib.extract import extract
from src.mylib.transform_load import load
from src.mylib.query import query


def test_extract():
    extracted_data = extract()
    assert extracted_data == "data/MH.csv"


def test_transform_load():
    transformed_loaded = load()
    assert transformed_loaded == "Success"


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
