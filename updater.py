import os
import requests
import zipfile
import io
import shutil
import pandas as pd

GITHUB_REPO = "AllenHuang03/TAP80029"
BRANCH = "main"
DATA_DIR = "data/observations"
ZIP_URL = f"https://github.com/{GITHUB_REPO}/archive/refs/heads/{BRANCH}.zip"

def download_latest_data():
    """
    Downloads and updates the latest observational data from the GitHub repository.
    """
    print("Fetching latest dataset from GitHub...")

    try:
        response = requests.get(ZIP_URL, stream=True)
        response.raise_for_status()  # Raise exception for HTTP errors (4xx, 5xx)

        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            extracted_dir = f"{GITHUB_REPO.split('/')[-1]}-{BRANCH}/data/"
            temp_dir = "temp_data"

            # Extract only data/ folder
            for file in z.namelist():
                if file.startswith(extracted_dir):
                    z.extract(file, temp_dir)

            # Move files to data/observations/
            source_dir = os.path.join(temp_dir, extracted_dir)
            if not os.path.exists(DATA_DIR):
                os.makedirs(DATA_DIR)

            for file in os.listdir(source_dir):
                shutil.move(os.path.join(source_dir, file), os.path.join(DATA_DIR, file))

            # Cleanup temp directory
            shutil.rmtree(temp_dir)

            print("✅ Data successfully updated!")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch dataset: {e}")
    
    except zipfile.BadZipFile:
        print("❌ Error: The downloaded file is not a valid ZIP archive.")

def verify_csv_data():
    """
    Reads the CSV file and ensures it can be processed.
    Skips commented header lines starting with '#'.
    """
    csv_path = os.path.join(DATA_DIR, "exoplanets.csv")
    if not os.path.exists(csv_path):
        print("⚠️ CSV file not found in the data directory.")
        return
    
    try:
        # Read CSV while ignoring '#' commented header lines
        df = pd.read_csv(csv_path, comment="#")
        print(f"✅ Successfully loaded CSV with {df.shape[0]} rows and {df.shape[1]} columns.")
        print(df.head(5))  # Show sample rows

    except Exception as e:
        print(f"❌ Error reading CSV: {e}")

if __name__ == "__main__":
    download_latest_data()
    verify_csv_data()
