import os
import shutil
import re
import requests
import time

yes_or_no = input("READY TO ORGANIZE .JPG FILES? YES OR NO: ").lower()

if yes_or_no == "yes":
    source_folder_path = input("What is the source folder path? ")
    destination_folder_name = input("What is the name of the destination folder? ")

    source_folder_path = rf"{source_folder_path}"
    destination_folder_path = rf"C:\Users\LOYAL\Desktop\{destination_folder_name}"

    os.makedirs(destination_folder_path, exist_ok=True)

    pattern = re.compile(r'.*\.jpg$', re.IGNORECASE)

    if not os.path.exists(source_folder_path):
        print(f"The source folder does not exist: {source_folder_path}")
        exit()

    for file in os.listdir(source_folder_path):
        if pattern.search(file):
            source_file_path = os.path.join(source_folder_path, file)
            destination_file_path = os.path.join(destination_folder_path, file)

            shutil.move(source_file_path, destination_file_path)
            print(f"Moved {file}")

    download = input("Do you want to save an image from the web? YES OR NO: ").lower()
    if download == "yes":
        link = input("Input the web link please: ")

        try:
            response = requests.get(link)
            response.raise_for_status()

            file_name = f"downloaded_{int(time.time())}.jpg"
            file_path = os.path.join(destination_folder_path,file_name)

            with open(file_path, "wb") as file:
                file.write(response.content)

            print(f"Image downloaded successfully to {destination_folder_path}")

        except requests.exceptions.RequestException as e:
            print("Error downloading image:", e)

else:
    print("Goodbye!!!")
