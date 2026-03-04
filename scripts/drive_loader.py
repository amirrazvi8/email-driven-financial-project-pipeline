import io
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

SERVICE_ACCOUNT_FILE = "key-file-path"
FOLDER_ID = "foder-id-key"


credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

drive_service = build("drive", "v3", credentials=credentials)

def list_files_in_folder(service, folder_id):
    files = []
    page_token = None

    while True:
        response = service.files().list(
            q=f"'{folder_id}' in parents and trashed = false",
            fields="nextPageToken, files(id, name, mimeType)",
            pageToken=page_token
        ).execute()

        files.extend(response.get("files", []))
        page_token = response.get("nextPageToken", None)

        if page_token is None:
            break

    return files

def download_file(service, file_id):
    request = service.files().get_media(fileId=file_id)
    file_stream = io.BytesIO()
    downloader = MediaIoBaseDownload(file_stream, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    file_stream.seek(0)
    return file_stream



files = list_files_in_folder(drive_service, FOLDER_ID)

print(f"Found {len(files)} files in folder.")

dataframes = []

for file in files:
    file_id = file["id"]
    file_name = file["name"]
    mime_type = file["mimeType"]

    print(f"Processing: {file_name}")

    try:

        if mime_type == "application/vnd.google-apps.spreadsheet":
            request = drive_service.files().export_media(
                fileId=file_id,
                mimeType="text/csv"
            )
            file_stream = io.BytesIO()
            downloader = MediaIoBaseDownload(file_stream, request)

            done = False
            while not done:
                _, done = downloader.next_chunk()

            file_stream.seek(0)
            df = pd.read_csv(file_stream)

        elif mime_type == "text/csv":
            file_stream = download_file(drive_service, file_id)
            df = pd.read_csv(file_stream)

        elif mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            file_stream = download_file(drive_service, file_id)
            df = pd.read_excel(file_stream)

        else:
            print(f"Skipped unsupported file type: {mime_type}")
            continue

        df["source_file"] = file_name
        dataframes.append(df)

    except Exception as e:
        print(f"Error processing {file_name}: {e}")



if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)
    print("Files combined successfully.")
else:
    combined_df = pd.DataFrame()
    print("No valid files found.")


combined_df