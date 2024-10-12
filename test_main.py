"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    extracted_data = extract()
    assert extracted_data == "data/MH.csv"


def test_transform_load():
    transformed_loaded = load()
    assert transformed_loaded == "Success"


def test_query():
    results = query("SELECT * FROM rr368_MentalHealth LIMIT 5")
    assert results == "Success"

if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_query()

