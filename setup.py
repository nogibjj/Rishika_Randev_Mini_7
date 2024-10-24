from setuptools import setup, find_packages

setup(
    name="databricksRishika",
    version="0.0.1",
    description="ETLQueryPipeline",
    author="Rishika Randev",
    author_email="rishika.randev@duke.edu",
    packages=find_packages(),
    install_requires=[
        "requests",
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
        "fire",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:fire.Fire()",
        ],
    },
)
