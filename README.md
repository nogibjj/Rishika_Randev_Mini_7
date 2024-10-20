[![CI](https://github.com/nogibjj/Rishika_Randev_Mini_6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Rishika_Randev_Mini_6/actions/workflows/cicd.yml)
# Rishika Randev's Python Script for IDS706 Week 7

## ☑️ Requirements (Mini Project 7):
1. Package a Python script with setuptools or a similar tool
2. Include a user guide on how to install and use the tool
3. Include communication with an external or internal database (NoSQL, SQL, etc)

## ☑️ The Dataset
The dataset used in this project shows the frequency of depression and anxiety symptoms for various different groups across the US over the course of 7 days (05/07 - 05/14) in 2020. It was collected by the U.S. Census Bureau as part of the Household Pulse Survey to capture the impact of COVID on Americans, and is freely available through data.gov at this link: https://catalog.data.gov/dataset/indicators-of-anxiety-or-depression-based-on-reported-frequency-of-symptoms-during-last-7-.

## ☑️ Steps
1. Prepare the necesary configuration files like the Dockerfile, devcontainer.json, Makefile, requirements.txt, and main.yml for GitHub Actions integration. Ensure that the requirements.txt lists all necessary packages (for example, python-dotenv and databricks-sql-connector for connecting to Databricks).
2. Create a library folder with extract, transform_load, and query python scripts.
   * The extract script pulls the above csv from the Internet, and writes the following data from it to the data folder:
       * Indicator, which represents whether the row's data is related to anxiety, depression, or both
       * Group, which is always "By State" in this case since I wanted to analyze the data statewise
       * State
       * Time Period Start Date, which is always 05/07/2020
       * Time Period End Date, which is always 05/14/2020
       * Value, which is the frequence value of the Indicator mentioned above
       * & High CI, which is the upper bound of the 95% confidence interval for this value
   * The transform_load script reads the csv from this data folder, connects to the external Databricks database, creates a table in it called rr368_MentalHealth, and then inserts the csv rows line by line into this table.
   * The query script includes a general function for executing any query input against this table.
4. Create a main.py script which allows for the query function to be called from the command line using the Python fire library. If no argument is provided, then by default calling the query function from the CLI results in execution of the complex query that is detailed below.
5. Create a test_main.py script which ensures that the ETL operations and the complex query run successfully.

## ☑️ Query

```sql
WITH t1 AS (
  SELECT
    Indicator,
    MAX(Value) Max_Value_Across_States
  FROM
    default.rr368_mentalhealth
  GROUP BY
    Indicator
)
SELECT
  t2.State,
  t2.Indicator,
  t2.Value,
  t1.Max_Value_Across_States,
  RANK() OVER(
    PARTITION BY t2.Indicator
    ORDER BY
      t2.Value DESC
  ) Value_Rank
FROM
  default.rr368_mentalhealth AS t2
  JOIN t1 ON (t1.Indicator = t2.Indicator)
LIMIT
  1000
```
The above query uses self joins, aggregations & grouping, as well as ordering within a window function. Specifically, it first creates a CTE which shows the max frequency value for each indicator type in the dataset. It then joins this output with select columns from the original datset, and also an additional column which shows the ranking for each row within its indicator group, with respect to the frequency value. The purpose is simply to show each row of the original dataset, along with the max value of the indicator group that that row belongs to, and also the rank of that row within its indiciator group. Interestingly, the results of this query showed that Mississippi was the state with the highest frequency of both depressive and anxiety disorder symptoms from that time period, based on this survey.

Databricks execution:

<img width="1230" alt="Screenshot 2024-10-13 at 12 14 49 AM" src="https://github.com/user-attachments/assets/5565b533-44b0-4a71-9edf-ec8395cc9d0a">



Execution from the command line, limited to the first three rows to reduce the output size. Please note that to avoid typing in the whole complex query from the CLI I have used it as the default arg for executing the query function from main:

<img width="1192" alt="Screenshot 2024-10-13 at 12 11 58 AM" src="https://github.com/user-attachments/assets/e086fd2a-94cf-4112-80ca-19b57bc50d72">


## ☑️ Demonstration of CLI Tool
The screenshot below shows how queries can be run against this dataset from the command line:

<img width="1174" alt="Screenshot 2024-10-13 at 12 30 22 AM" src="https://github.com/user-attachments/assets/a1d2b069-d935-46a8-b6d0-b697cb469061">





