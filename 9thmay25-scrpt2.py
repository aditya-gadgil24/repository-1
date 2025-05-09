import pandas as pd
from google.cloud import storage
from pathlib import Path

# Step 1: Read the local Parquet file using pyarrow engine
local_parquet_path = 'C:\\Users\\adity\\Desktop\\houseprice.parquet'
df = pd.read_parquet(local_parquet_path, engine="pyarrow")

# Display the DataFrame (optional)
print(df.head())

# Writing data to temp parquet file
df.to_parquet('tempdata.parquet', engine='pyarrow')

# Step 2: Upload the file to Google Cloud Storage
bucket_name = "mangobuckit"  # Replace with your bucket name
destination_blob_name = "mangobuckit/sample_data.parquet"  # GCS object path

# Initialize the GCS client using Application Default Credentials (from gcloud auth login)
client = storage.Client()
bucket = client.bucket('mangobuckit')
blob = bucket.blob(destination_blob_name)

# Upload the local file
blob.upload_from_filename('C:\\Users\\adity\\Desktop\\houseprice.parquet')

print(f"File uploaded to gs://{'mangobuckit'}/{'mangobuckit/sample_data.parquet'}")

"""The script read data from parquet file stored in local directory into pandas df using pyrrow, wrote to
a temp parquet file, loaded the file into blob object using gcs client"""


