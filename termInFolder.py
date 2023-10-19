import os

# 找出資料夾裏含有關鍵字的檔案名稱
# loop through all the files in the folder and print file name that contain keyword for search 
# Define the folder path and the search term
folder_path = '/folder/Path'
search_term = 'keyword'

# Function to search for the term in a file
def search_in_file(file_path, search_term):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line_number, line in enumerate(file, start=1):
            if search_term in line:
                return line_number
    return None

# Loop through all files in the folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        line_number = search_in_file(file_path, search_term)
        if line_number is not None:
            print(f"Found '{search_term}' in '{file_path}' (Line {line_number})")

# Note: Replace '/path/to/your/folder' with the actual path to your folder
