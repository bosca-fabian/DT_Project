import pandas as pd
import numpy as np
import sys


input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

#rename for next file source_system of 2023 schema in source from 2022 schema
if input_file.endswith("2023.csv"):
    if 'source_system' in df.columns:
        df = df.rename(columns={'source_system' : 'source'})

#make negative values positive
df['value'] = df['value'].abs()

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

#convert status all to lower
df['status'] = df['status'].astype(str).str.lower()

#Write to file
df.to_csv(output_file, index=False, date_format='%Y-%m-%d', na_rep="NULL")

