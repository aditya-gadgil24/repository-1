"""This file and its code blocks will demonstrate use of EL architecture pattern for
data pipeline illustrating different use cases and scenarios"""


# Code blocks promote modularity and reusability

# EL pipeline to read data from csv file on local file system, write to postgresql table

"""logic for reading data from local file system"""
# importing libraries
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
# reading data from local file system
df = pd.read_csv('C:\\Users\\adity\\Desktop\\hdfs\\social.csv')
print(df)
print(df.head())

# logic for memory map of the dataframe columns
memodel = df.info(memory_usage='deep')
print(memodel)
# end

# Logic for writing data to postgresql table
db_user = "postgres"
db_password = "Bigtable24$"
db_host = "localhost"
db_port = 5432
db_name = "postgres"
table_name = "social"

# Creating SQLAlchemy engine

engine = create_engine("postgresql+psycopg2://postgres:Bigtable24$@localhost:5432/postgres")                                                           
# Load data to postgresql table
sqldata = df.to_sql('social', con=engine, if_exists='replace', index=False)
print(sqldata)
# end


"""This small script has successfully read data from local file system, pre-processed it in Pandas
and then written it to postgresql db table. The pipeline output has been verified running select query
in postgresql table where the data was written"""

# End of this sub script


"""This sub script and its code blocks will read data from parquet file stored in local file system
and write it to google cloud storage bucket after some processing"""

# The extraction layer will involve the local directory where the file is stored

import pandas as pd
import pyarrow
from google.cloud import storage

# Reading data from local directory
df = pd.read_parquet('C:\\Users\\adity\\Desktop\\houseprice.parquet', engine="pyarrow")
print(df)
# Printing the data from file





