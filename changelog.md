# Changelog

## [1.0] - 2026-01-02

### Added
- **Automated Workflow**: Implemented a complete Snakemake pipeline with five stages: initial_validation -> normalization-> imputation -> deduplication -> final_validation.
- **Schema Evolution Support**: Added logic to handle structural differences between 2022 and 2023 records, including column renaming and expansion.
- **Integrity Checks**: Generated SHA-256 checksums for raw files and added verification documentation in `docs/Integrity/integrity_notes.md`.
- **Secondary Format Export**: Configured the final stage to save processed data in both CSV and JSON formats.
- **Environment Capture**: Created `requirements.txt` and documented the `pip/venv` setup instructions for full reproducibility.

### Changed
- **Folder Structure**: Reorganized the project into the required standard structure (`data/`, `src/`, `docs/`, `reports/`, `workflow/`).
- **Validation Logic**: Updated `validate.py` to output readable text summaries for the pipeline reports.
- **Documentation**: Expanded the `README.md` to include detailed project purpose and dataset descriptions.

### Fixed
- **DataFrame Output Error**: Resolved a `TypeError` where `f.write()` was incorrectly passed a DataFrame object instead of a string.
- **Deduplication Logic**: Corrected the script to properly drop duplicate records while preserving the original raw file integrity.
- **CSV Formatting**: Fixed "phantom column" issues by ensuring `index=False` is used in all CSV exports.