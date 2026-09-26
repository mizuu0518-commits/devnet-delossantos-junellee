"""
Module 2 — Activity: File Sorting with os and shutil
Student: Delos Santos, Junelle
Date: 9/26/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I built a file sorting program that automatically organizes files into different folders based on their file extensions. 
I used the file extension as the rule for sorting the files.


============================================
KEY VOCABULARY
============================================
- os module: a Python module used to interact with files, folders, and the operating system.
- shutil module: a Python module used to move, copy, and manage files and folders.
- file path: the location of a file or folder on a computer.
- directory: a folder that contains files or other folders.
- extension: identifies the file’s format and tells the operating system which application can open it.


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""


# --- paste your existing code here ---
import os
import shutil

source_folder = "files"
 
for filename in os.listdir(source_folder):
 
    if filename.endswith((".jpg", ".png")):
        folder = "Images"
 
    elif filename.endswith((".txt", ".pdf")):
        folder = "Documents"
 
    else:
        folder = "Others"
 
    destination = source_folder + "/" + folder
 
    os.makedirs(destination, exist_ok=True)
 
    shutil.move(source_folder + "/" + filename,
                destination + "/" + filename)
 
print("Files sorted!")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
At first I was confused about the file path and folder location. 
The program will not work if the source folder does not exist or if the path is incorrect. 
I learned that I need to make sure the folder name and file path are correct before running the program.
Also, to have a existing files ready.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
