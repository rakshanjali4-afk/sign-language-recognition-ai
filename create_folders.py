import os
import string

base_folder = "dataset"

# create dataset folder
os.makedirs(base_folder, exist_ok=True)

# create A-Z folders
for letter in string.ascii_uppercase:
    folder_path = os.path.join(base_folder, letter)
    os.makedirs(folder_path, exist_ok=True)

print("A–Z folders created successfully!")
