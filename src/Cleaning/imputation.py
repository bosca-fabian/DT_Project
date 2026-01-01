import pandas as pd
import numpy as np
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

#drop any rows that have nan in value column
df = df.dropna(subset=['value'])

#fill any nans from mentioned columns with placeholder
df['unit'] = df['unit'].fillna('CHK')
df['source'] = df['source'].fillna('import_batch')
df['status'] = df['status'].fillna('review')

if input_file.endswith("2023.csv"):
    if 'department' in df.columns:
        df['department'] = df['department'].fillna('ADMIN')
    if 'priority' in df.columns:
        df['priority'] = df['priority'].fillna('high')

df.to_csv(output_file, index=False)

