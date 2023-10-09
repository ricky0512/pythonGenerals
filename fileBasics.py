import os
import glob

def findLatestFile(directory, pattern, tf=True, ext=".html"):
    # single line could solve this too
    # latestFile = max(glob.glob(os.path.join(directory, f"*{pattern}*.html")), key=os.path.getmtime, default=None)

    # Create a list of files in the directory that match the pattern
    file_list = glob.glob(os.path.join(directory, f"*{pattern}*{ext}"))

    # Check if there are any matching files
    if not file_list:
        return None  # No matching files found

    # Sort the list of files by modification time in descending order
    file_list.sort(key=os.path.getmtime, reverse=tf)

    # Return the latest file
    return file_list[0]

def readFile(file_path, encoding='utf-8'):
    """
    Read the contents of a file and return them as a string.

    Args:
        path (str): The path to the directory containing the file.
        filename (str): The name of the file to be read.
        encoding (str, optional): The encoding of the file (default is 'utf-8').

    Returns:
        str: The contents of the file as a string.
    """
    # file_path = os.path.join(path, filename + ext)

    try:
        with open(file_path, 'r', encoding=encoding) as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def replace_multiple(input_string, replacements):
    for old, new in replacements:
        input_string = input_string.replace(old, new)
    return input_string

def write2File(dir, fileName, content, encoding='utf-8'):
    with open(f"{dir}/{fileName}", 'w', encoding=encoding) as file:
        file.write(content)

# configs
dir = r"D:\download"
pattern = r"ffff"
myext = r".html"
encoding = r'utf-8'
replacements = [
    ('</div><td field=', '</div></td><td field='),
    ('</div><tr id=row', '</div></td></tr><tr id=row'),
    ('</table></div><div class=footer', '</td></tr></tbody></table></div><div class=footer')
]
outputFile = 'fireDept.html'
outF = os.path.join(dir,outputFile)
targetClass = 'datagrid-view2'
datagridFile = 'datagrid.html'
datagridF = os.path.join(dir,datagridFile)

# fName = os.path.join(dir,pattern + myext)
# print(fName)

fName = findLatestFile(dir, pattern, True, myext)
print(fName)

file_contents = readFile(fName, encoding='utf-8')
if file_contents:
    # print(file_contents)
    # Your list of replacement pairs

    # Your input string
    # Replace the substrings in the input string
    result = replace_multiple(file_contents, replacements)

    # Print the result
    # print(result)
    write2File(dir, outputFile, result, encoding='utf-8')
    # print(f"file write to {outF}")

else:
    print("Failed to read the file.")

