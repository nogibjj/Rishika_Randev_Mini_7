
## Python Package User Guide
The ETL and querying functionality is packaged into a Python package called databricksRishika.

## Set Up Package
The dataset used in this project shows the frequency of depression and anxiety symptoms for various different groups across the US over the course of 7 days (05/07 - 05/14) in 2020. It was collected by the U.S. Census Bureau as part of the Household Pulse Survey to capture the impact of COVID on Americans, and is freely available through data.gov at this link: https://catalog.data.gov/dataset/indicators-of-anxiety-or-depression-based-on-reported-frequency-of-symptoms-during-last-7-.

## Use it For ETL & Querying
1. Prepare the necesary configuration files like the Dockerfile, devcontainer.json, Makefile, requirements.txt, and main.yml for GitHub Actions integration. Ensure that the requirements.txt lists all necessary packages (for example, python-dotenv and databricks-sql-connector for connecting to Databricks).
2. Create a library folder with extract, transform_load, and query python scripts.
3. Create a main.py script which allows for the query function to be called from the command line using Python argparse. 
4. Create a test_main.py script which ensures that the ETL operations and querying the Databricks database run successfully.
5. Create a setup.py file to use setuptools to create a package for your Python functionality.
6. Set up the Python package and run the ETL and querying functionalities from the CLI using this user guide.

