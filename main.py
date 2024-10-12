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
    if input == None:
        input = "WITH "
    query(input)


if __name__ == "__main__":
    fire.Fire()
