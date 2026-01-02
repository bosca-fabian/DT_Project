import pandas as pd
import sys
import numpy as np
import pandera as pa
from datetime import date


expected_schema = pa.DataFrameSchema(
    {
    'record_id': pa.Column(str, coerce=True, required=True),
    'date' : pa.Column(pa.DateTime, coerce=True),
    'category': pa.Column(str, coerce=True, required=True),
    'value' : pa.Column(float, pa.Check(lambda x: x >= 0)),
    'unit' : pa.Column(str, coerce=True, required=True),
    'source' : pa.Column(str, coerce=True, required=False),
    'source_system' : pa.Column(str, coerce=True, required=False),
    'status' : pa.Column(str, coerce=True, required=True),
    'department' : pa.Column(str, coerce=True, required=False),
    'priority' : pa.Column(str, coerce=True, required=False)
})

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file)

year = re.search(r"\b(2022|2023)\b", input_file)

report_md = f"""# Data Quality Report: {year}
## Summary
- **Date Processed:** {date.today}
- **Source File:** {input_file}
## Results:\n"""

try:
    expected_schema.validate(df, lazy=True)
    with open(output_file, "w") as f:
        f.write(report_md)
        f.write("Schema validation passed! + all values within fields are proper.")
    
except pa.errors.SchemaErrors as err:
    
    errors_df = err.failure_cases

    with open(output_file, "w") as f:
        f.write(report_md)
        f.write("\n--- Summary of Errors ---")
        f.write(errors_df[['column', 'check', 'failure_case', 'index']].to_string())

