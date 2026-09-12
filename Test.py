import os
import shutil


folder_path = input("Enter the folder path to organize: ")


if not os.path.exists(folder_path):
    print(f"Error: The directory '{folder_path}'  not exist.")
else:
    
    all_items = os.listdir(folder_path)

    
    images = 0
    documents= 0
    videos= 0
    others= 0

categories = ["Images", "Document", "Videos", "Others"]


