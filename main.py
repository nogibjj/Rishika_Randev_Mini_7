"""
ETL-Query script
"""

import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "query",
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)

    if args.action == "query":
        parser.add_argument("added_query")

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        extract()
        print("Done")
    elif args.action == "transform_load":
        load()
        print("Done")
    elif args.action == "query":
        query(args.added_query)

    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()






# """
# ETL-Query script
# """

# from mylib.extract import extract
# from mylib.transform_load import load
# from mylib.query import query
# import fire


# def etl():
#     extract()
#     load()


# def complex_query(input=None):
#     print(f"Input received: {input}")
#     if input is None:
#         input = "WITH t1 AS (SELECT Indicator, MAX(Value) Max_Value_Across_States \
#         FROM default.rr368_mentalhealth \
#         GROUP BY Indicator) \
#         SELECT t2.State, t2.Indicator, t2.Value, \
#         t1.Max_Value_Across_States, \
#         RANK() OVER(PARTITION BY t2.Indicator ORDER BY t2.Value DESC) Value_Rank \
#         FROM default.rr368_mentalhealth AS t2 \
#         JOIN t1 \
#         ON (t1.Indicator = t2.Indicator) \
#         LIMIT 3"
#     query(input)


# if __name__ == "__main__":
#     fire.Fire({
#         'etl': etl,
#         'complex_query': complex_query,
#     })
