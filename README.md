## SQLite Lab

![4 17-etl-sqlite-RAW](https://github.com/nogibjj/sqlite-lab/assets/58792/b39b21b4-ccb4-4cc4-b262-7db34492c16d)

[![CI](https://github.com/nogibjj/Rishika_Randev_MiniProject_1/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Rishika_Randev_MiniProject_1/actions/workflows/hello.yml)

# Rishika Randev's Python & SQLite Script for IDS706 Week 5

## ☑️ Requirements (Mini Project 5):
1. Connect to a SQL database
2. Perform CRUD operations
3. Write at least two different SQL queries

## ☑️ The Dataset
The dataset used in this project shows diet, physical activity, and nutrition data from the behaviorial risk factors survey across the US in 2023. It is published by the U.S. Department of Health & Human Services and freely available through data.gov at this link: https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system.

## ☑️ Steps
1. Prepare the necesary configuration files like the Dockerfile, devcontainer.json, Makefile, requirements.txt, and main.yml for GitHub Actions integration. Ensure that the requirements.txt lists all necessary packages (for example, fire for the CLI).
2. Create a library folder with extract, transform_load, and query python scripts.
   * The extract script pulls the behaviorial risk factors csv from the Internet and writes its first 10 rows and specific columns (Year Start, Year End, Location Abbrevation, Location Description, Survey Question, and Data Value) to the data folder.
   * The transform_load script reads the csv from this data folder, creates a table in a local SQLite database called Behaviors and inserts the csv rows line by line into Behaviors.
   * The query script includes functions for reading all or a select number of rows from the Behaviors table, deleting a row from the table based on row ID, updating a row from the table based on row ID, and creating a new row.
4. Create a main.py script which allows for the query functions to be called from the command line using the Python fire library.
5. Create a test_main.py script which ensures that the CRUD operations from the query script run successfully.

The screnshots below demonstrate the use of the command line for querying the Behaviors table:
   ![Sample Stats](https://github.com/user-attachments/assets/54a6c401-c230-46b9-948d-0e2929d952f4)
   * test_generate_data_viz(csv): calls generate_data_viz() using the student performance factors csv file in order to produce the below scatterplot.
     
     ![Visualization](performance.png)



