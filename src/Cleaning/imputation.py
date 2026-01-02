import pandas as pd
import numpy as np
import sys

# input_file = ("data/interim/normalized_records_2022.csv")
input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

#remove rows where value is null
df = df.dropna(subset=['value'])

#fix different nulls
# df['unit'] = df['unit'].str.replace(r'NULL', 'CHK', regex=True)
# df['source'] = df['source'].str.replace(r'NULL', 'import_batch', regex=True)
# df['status'] = df['status'].str.replace(r'NULL', 'review', regex=True)


df['unit'] = df['unit'].fillna('CHK')
df['source'] = df['source'].fillna('import_batch')
df['status'] = df['status'].fillna('review')

if input_file.endswith("2023.csv"):
    if 'department' in df.columns:
        df['department'] = df['department'].fillna('ADMIN')
    if 'priority' in df.columns:
        df['priority'] = df['priority'].fillna('high')


#Write to file
df.to_csv(output_file, index=False)

