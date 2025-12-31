import pandas as pd
import numpy as np

input_file = ("data/raw/records_2022.csv")

df = pd.read_csv(input_file)

#remove needless whitespaces
df = df.apply(lambda x: x.astype(str).str.strip())

#make missing values numpy nans
df = df.replace(['nan', ''], np.nan)

#convert to datetime dtype so when it's written it automatically goes to desired format
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='raise', format='mixed')

#convert categories all to lower
df['category'] = df['category'].astype(str).str.lower()

#fix different formats found in categories
df['category'] = df['category'].str.replace(r'[^a-z]+', '_', regex=True)
df['category'] = df['category'].str.replace(r'labtest', 'lab_test', regex=True)

#make negative values positive
df['value'] = df['value'].abs()

#convert status all to lower
df['status'] = df['status'].astype(str).str.lower()

#Write to file
df.to_csv("data/interim/normalized_records_2022.csv", index=False, date_format='%Y-%m-%d')

