# ETL SCRIPT
# READ PROCESS TRANSFORM LOAD


"""Read CSV file from local directory, process, write to a new file or export to GCS bucket"""

# READING DATA FROM LOCAL DIRECTORY
import pandas as pd
df = pd.read_csv('C:\\Users\\adity\Desktop\\reservoir\\store_orders.csv')
print(df.head())

# DATA viewing and inspection
shape = df.shape
print(shape)

tail = df.tail()
print(tail)

info = df.info()
print(info)

des = df.describe()
print(des)

# DATA cleaning
errors = df.duplicated()
print(errors)
clean_errors = df.drop_duplicates()
print(clean_errors)
null = df.isnull()
print(null)
find_na = df.dropna()
print(find_na)
replace_na = df.fillna(value=100)
print(replace_na)


# DATA transformation
df['order_type'] = df['order_type'].str.upper()
print(df['order_type'])

df['order_date'] = df['order_date'].str.strip()
print(df['order_date'])

df['bill_amt'] = df['order_amt'] + df['service_charge']
print(df['bill_amt'])

df['bill_amt'] = df['bill_amt'].astype('int32')
print(df['bill_amt'])

df['final_bill'] = df['bill_amt'] - df['promotional_disc']
print(df['final_bill'])

df = df.drop(columns=['order_type'])
print(df)

df = df.rename(columns={'order_id' : 'order_sequence'})
df = df.rename(columns={'service_charge' : 'sc'})
print(df.head())

# Adding gst to the final bill for payable amt
gst_rate = 0.18
df['payable_amt'] = df['final_bill'] * (1 + gst_rate)
print(df.tail())

# WRITING the processed data to a new file
newdf = df.to_csv('C:\\Users\\adity\Desktop\\reservoir\\processed_data.csv', index='False')
print(newdf)
parquet_f = df.to_parquet('C:\\Users\\adity\\Desktop\\output.parquet')
print(parquet_f)


"""End of script"""