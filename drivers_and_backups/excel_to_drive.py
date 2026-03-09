"""
Created on Mon Feb 13 11:03:12 2024

@author: antonioyepez
"""

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# AUTH
SCOPES = ['https:www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'key.json'

# Load credentials and initialize the Drive API service
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)

# Uploads a local excel file and triggets an automatic conversion to a google spreadsheets in the cloud.
def upload_excel_to_gsheet(excel_file_path, gsheet_name):
    # Setting 'mimeType' to 'google-apps.spreadsheet' tells Google Drive to convert the incoming binary Excel file into an editable Sheet
    to convert the incoming binary Excel file into an editable Sheet.
    file_metadata = {
        'name': gsheet_name,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    # Prepare media for upload
    media = MediaFileUpload(excel_file_path,
                            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                            resumable=True)

    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    
    print(f'File ID: {file.get("id")}')
    return file.get("id")

excel_file_path = 'file.xlsx'
gsheet_name = 'Migrated Google Sheet'

upload_excel_to_gsheet(excel_file_path, gsheet_name)
