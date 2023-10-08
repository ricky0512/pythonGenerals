# 檔案, 刪除, 資料夾, 路徑, 建立時間, 修改時間, 時間戳, 轉換, 年月日, 時分秒
import os
import glob
import datetime
import shutil

def findLatestFile(directory, pattern,ext=".htm"):
    # Create a list of files in the directory that match the pattern
    fileList = glob.glob(os.path.join(directory, f"*{pattern}*{ext}"))

    # Check if there are any matching files
    if not fileList:
        return None  # No matching files found

    # Sort the list of files by modification time in descending order
    fileList.sort(key=os.path.getmtime, reverse=True)

    # Return the latest file
    return fileList[0]

def getFileCreateTime(filePath):
    # Get the creation and modification datetime of the file
    statInfo = os.stat(filePath)
    print(f"stat info: {statInfo}")
    creationTime = statInfo.st_ctime
    return creationTime

def convertTimeReadable(timestamp):
    # Convert the timestamp to a datetime object
    dt_object = datetime.datetime.fromtimestamp(timestamp)

    # Extract Year, Month, Day, Hour, Minute, and Second
    year = dt_object.year
    month = dt_object.month
    day = dt_object.day
    hour = dt_object.hour
    minute = dt_object.minute
    second = dt_object.second

    return year, month, day, hour, minute, second

def deleteFilesExceptLatest(path, pattern, extension):
    # Create a list of all files in the directory matching the pattern and extension
    files = glob.glob(os.path.join(path, f"*{pattern}*{ext}"))
    
    # Ensure there are files to delete
    if len(files) <= 1:
        print("No files to delete or only one file found. Nothing to do.")
        return
    
    # Sort the files by modification time in descending order
    files.sort(key=os.path.getmtime, reverse=True)
    
    # Keep the latest file and delete the rest
    latest_file = files[0]
    for file in files[1:]:
        os.remove(file)
        print(f"Deleted: {file}")

    print(f"Kept latest file: {latest_file}")




# config file path, key word, and extension of target file
dir = r"C:\somewhere\Downloads"
pattern = "Keyword"
ext = '.htm'

# find the latest File in the directory with path, keyword, extension
fName = findLatestFile(dir, pattern, ext)
print(f"file name: {fName}")
# similar to this:
# fName = max(glob.glob(os.path.join(directory, f"*{pattern}*.{ext}")), key=os.path.getmtime, default=None)

# get the create time of certain file
creteTime = getFileCreateTime(fName)    # in seconds
print(f"create time: {creteTime}")

# get timestamp in seconds to readable parameters
year, month, day, hour, minute, second = convertTimeReadable(creteTime)
print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}")
print(f"{type(year)}")

# delete all the files in the directory by pattern and extension but exclude the latest one 
deleteFilesExceptLatest(dir, pattern, ext)
