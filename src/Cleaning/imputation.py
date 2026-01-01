import pandas as pd
import numpy as np

input_file = ("data/interim/normalized_records_2022.csv")

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

#Write to file
df.to_csv("data/interim/imputated_records_2022.csv", index=False)

