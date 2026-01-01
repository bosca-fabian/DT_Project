import pandas as pd
import numpy as np
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

#drop duplicates based on id
df = df.drop_duplicates(subset=['record_id'], keep='first')

df.to_csv(output_file, index=False)