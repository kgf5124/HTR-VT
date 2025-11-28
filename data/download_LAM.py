import os
import shutil

drive_path = "/content/drive/MyDrive/LAM_formatted/lines"
target_path = "/content/HTR-VT/data/LAM/lines"

if not os.path.exists(drive_path):
    raise FileNotFoundError(
        f"Dataset not found at {drive_path}.\n"
        "Please upload the formatted LAM dataset folder to Google Drive:\n"
        "MyDrive/datasets/LAM_formatted/lines"
    )

os.makedirs(target_path, exist_ok=True)

shutil.copytree(drive_path, target_path, dirs_exist_ok=True)

print("Dataset copied to HTR-VT/data/LAM/lines/")
