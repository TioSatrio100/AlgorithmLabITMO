import os
import subprocess

# Root folder
root_folder = "."

# find all file in folder
for dirpath, _, filenames in os.walk(root_folder):
    for file in filenames:
        if file.endswith(".py") and file != "run_all.py":  # don't run this file
            file_path = os.path.join(dirpath, file)
            print(f"Running {file_path}...")
            subprocess.run(["python", file_path])
