import pandas as pd
import numpy as np

input_file = ("data/interim/imputated_records_2022.csv")

df = pd.read_csv(input_file)

df = df.drop_duplicates(subset=['record_id'], keep='first')

df.to_csv("data/processed/final_records_2022.csv", index=False)