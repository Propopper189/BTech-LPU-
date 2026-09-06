import os
from datetime import datetime

DATA_DIR = "/data"
FILE_PATH = os.path.join(DATA_DIR, "uploads.txt")

os.makedirs(DATA_DIR, exist_ok=True)

def write_sample_data():
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"Sample upload stored at {datetime.now()}\n")
    print("Data written successfully.")

def read_data():
    if os.path.exists(FILE_PATH):
        print("\nStored file content:\n")
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("No stored data found.")

print("Application started.")
write_sample_data()
read_data()