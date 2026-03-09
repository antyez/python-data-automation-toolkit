# Python Data Automation & ETL Toolkit

A comprehensive collection of Python scripts developed to automate high-volume data operations, system directory provisioning, and cloud-to-local synchronization. 

## Proven Business Impact
These tools were engineered and deployed within a top-tier European consumer electronics company to manage complex product databases and international catalogs.
* **Scale:** Optimized workflows for a catalog serving multiple international markets.
* **Efficiency:** Reduced manual data partitioning and folder management by over 90%.
* **Data Quality:** Implemented NLP-based validation to ensure linguistic consistency in multilingual technical documentation.

## Key Modules

### 1. Linguistic Validator (`language_validator.py`)
A Data Quality Assurance (DQA) tool that uses Natural Language Processing to identify human errors in localized datasets.
* **NLP Integration:** Uses `langdetect` to verify if the content matches the target ISO language code.
* **Visual Auditing:** Automatically highlights cells with inconsistencies in red using `openpyxl`.
* **Exception Reporting:** Generates a standalone "Pending Review" file for stakeholders to address errors without stopping the main pipeline.

### 2. Cloud Backup Manager (`drive_backup.py`)
Implements a robust Cloud-to-Cloud backup strategy for business continuity.
* **API Integration:** Connects to Google Drive and Sheets APIs using Service Accounts.
* **Version Control:** Exports live Google Sheets to Excel (.xlsx) binaries and archives them with timestamped naming conventions.
* **Memory Optimization:** Handles file streams in-memory using `io.BytesIO` for high-speed execution.

### 3. Dataset Splitter (`split_by_language.py`)
Automates data partitioning for international teams.
* **Pandas Powered:** Uses high-performance boolean indexing to segment master files into language-specific exports.
* **Integrity:** Forces specific dtypes (like IDs) to strings to prevent data corruption during the export process.

### 4. Bulk Directory Engine (`bulk_folder_creator.py`)
Bridges the gap between data records and physical file systems.
* **System Automation:** Reads Excel metadata to generate standardized folder structures based on a "Root Template".
* **OS Compatibility:** Implements string normalization (replacing spaces with underscores) to ensure path stability across Windows, macOS, and Linux.

### 5. Excel to Sheets Synchronizer (`excel_to_drive.py`)
Closes the loop between local analysis and cloud collaboration.
* **Automated Migration:** Uploads local Excel reports and triggers a native conversion to Google Sheets format.
* **Resumable Uploads:** Configured for high reliability even with large datasets.

## Tech Stack
* **Language:** Python 3 (Version 3.9, 3.10 & 3.11)
* **Data Libraries:** `pandas`, `openpyxl`
* **Cloud APIs:** `google-api-python-client`, `google-auth`
* **NLP:** `langdetect`
* **System:** `shutil`, `os`, `io`

## Setup & Installation (Anaconda & Spyder)

This project is optimized for the Anaconda ecosystem. To run these scripts using the Spyder IDE, follow these simple steps:

1. Open Anaconda Navigator and launch Spyder.
2. Install necessary libraries via the Anaconda Prompt or Spyder's internal console:
   ```bash
   pip install pandas openpyxl google-api-python-client google-auth-httplib2 google-auth-oauthlib langdetect
3. Change the URLs.
4. Press "Run".
