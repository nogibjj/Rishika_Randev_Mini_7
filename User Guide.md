
## Python Package User Guide
The ETL and querying functionality is packaged into a Python package called databricksRishika.

## Set Up Package
After cloning the repository, run the below command from the terminal to set up the package and use it from the CLI.
```bash
python setup.py develop
```

## Use it For ETL & Querying
The general format for CLI commands will be:
```bash
etl <action>
```
The available actions are:
* extract (pull the online csv to your local)
* transform_load (transform and load the csv to a Databricks db)
* query <argument> (query the Databricks database)

For example:
```bash
etl extract
```

<img width="480" alt="Screenshot 2024-10-24 at 12 17 38 PM" src="https://github.com/user-attachments/assets/6de7593e-89e1-4aaf-be0f-df31691581f1">


```bash
etl transform_load
```

<img width="727" alt="Screenshot 2024-10-24 at 12 18 27 PM" src="https://github.com/user-attachments/assets/6405096f-fb4a-4d95-96ec-09854c3b2134">


```bash
etl query "SELECT Indicator, AVG(Value) Avg_Value_Across_States FROM default.rr368_mentalhealth GROUP BY Indicator"
```

<img width="1174" alt="Screenshot 2024-10-24 at 12 18 47 PM" src="https://github.com/user-attachments/assets/70ccf5f7-414c-4d97-aec1-f411c67c69a0">


## Note:
These commands can also be run through the Makefile, for example:
```bash
make etl
```
<img width="719" alt="Screenshot 2024-10-24 at 12 15 30 PM" src="https://github.com/user-attachments/assets/affc738a-a256-485e-a03a-2d2a7e6d3133">


```bash
make query
```
<img width="1170" alt="Screenshot 2024-10-24 at 12 15 38 PM" src="https://github.com/user-attachments/assets/cee6dd23-05f8-4181-bf4a-4fbe446c4886">



In this case, "make etl" combines the extract, transform, and load steps. Also, "make query" uses the below default query instead of allowing for a custom argument from the CLI.

```bash
SELECT Indicator, MAX(Value) Max_Value_Across_States FROM default.rr368_mentalhealth GROUP BY Indicator
```

