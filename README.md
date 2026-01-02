# DT_Project

### Project overview

The primary goal of this project is to build a research-grade, reproducible data repository that automates the cleaning and validation of a sensitive local dataset.This repository is designed to ensure that any researcher or team member can clone the project and obtain identical results, including cleaned data, validation logs, and summary reports, with a single command.


### Folder structure

This project follows a standard organized structure to ensure reproducibility and clarity:

* **data/** contains the .csv and .json and these are separated in 3 subfolders: raw(initial immutable data), interim(data going through cleaning process) and processed(final data). 
* **docs/** includes metadata information + integrity checks, format choices and notes
* **reports/** contains in a subfolder validation results of the schema of the dataset initially and after the processing of the dataset to ensure that after everything is done the dataset and the data within the dataset are correct.
* **src/** contains subfolders with associated scripts
* **workflow** has the files associated with the pipeline
* **other relevant files** can be found in the main folder like requirements to run the project, license, changelog 


### Dataset Characteristics
The dataset contains with several "messy" features:
* **Quality Issues**: Includes missing values, duplicated record IDs, and inconsistent category strings such as case or whitespace variants.
* **Integrity Challenges**: Contains occasional outliers and invalid values, such as negative numbers.
* **Schema Evolution**: Structural differences exist between the 2022 and 2023 data files.

### File Specifications
The raw data consists of two primary files:
* **records_2022.csv**: Contains columns for `record_id`, `date`, `category`, `value`, `unit`, `source`, and `status`.
* **records_2023.csv**: Includes expanded columns such as `source_system`, `department`, and `priority`.

## Reproducibility Instructions

### Environment Setup
This project uses `pip` and `venv` for environment management. To recreate the environment:
1. **Create a virtual environment**: `python -m venv venv`
2. **Activate the environment**:
   * Windows: `.\venv\Scripts\activate`
   * macOS/Linux: `source venv/bin/activate`
3. **Install dependencies**: `pip install -r requirements.txt`

### Running the Pipeline
The entire workflow is automated. To rebuild all outputs from raw data, run:
   `snakemake -c2`

### Release Version

This repository is currently at `v1.0`.

### Citations

No citation needed. The chosen license allows free use of the project, code, whatever, however one desires. I don't care what you do with it.