# 排程, 函式, 資料夾, 路徑, 檔名, 關鍵字, 間隔, 年月日, 時分, 指定時間
import glob
import os
import time
from datetime import datetime, timedelta
import schedule


def deleteFilesExceptLatest(path, pattern, ext):
    # Create a list of all files in the directory matching the pattern and extension
    files = glob.glob(os.path.join(path, f"*{pattern}*{ext}"))
    # print(f"files: {files}")
    
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

def deleteFilesByPattern(path, pattern, ext):
    # Create a list of all files in the directory matching the pattern and extension
    files = glob.glob(os.path.join(path, f"*{pattern}*{ext}"))
    # print(f"files: {files}")

    # Ensure there are files to delete
    if len(files) <= 0:
        print("No files to delete or only one file found. Nothing to do.")
        return
    
    latest_file = files[0]
    for file in files:
        os.remove(file)
        print(f"Deleted: {file}")

    print(f"Kept latest file: {latest_file}")

# Function to schedule tasks from the list of tuples
# DO and then loop mode
def schedule_tasks():
    current_time = scheduled_time = datetime.now()
    for item in tasks:
        if item[1] == 'at':
            _, _, func, *args = item
            func(*args)
        elif isinstance(item[0], int):  # Interval-based task
            interval, unit, func, *args = item
            # DO session IF NOT DO and then loop mode move this session after unit session 
            # Calculate the time remaining until the next scheduled execution
            time_remaining = (scheduled_time - current_time).total_seconds()

            # If the time remaining is non-negative, schedule the task
            if time_remaining >= 0:
                schedule.every(time_remaining).seconds.do(func, *args)
            # DO session END

            # unit session
            if unit == 'year':
                scheduled_time = current_time.replace(year=current_time.year + interval)
            elif unit == 'month':
                scheduled_time = current_time.replace(month=current_time.month + interval)
            elif unit == 'day':
                scheduled_time = current_time + timedelta(days=interval)
            elif unit == 'hour':
                scheduled_time = current_time + timedelta(hours=interval)
            elif unit == 'minute':
                scheduled_time = current_time + timedelta(minutes=interval)
            else:
                continue  # Skip invalid units
            # unit session END

# Define the schedule tasks in a list of tuples
cleanDir = r'C:\path\somewhere'
pattern = f'keyword'
ext = r'.txt'
tasks = [
    ('11:57:00', 'at', deleteFilesExceptLatest, cleanDir, pattern, ext)
]



# Run the scheduler in an infinite loop
while True:    
    # Schedule the tasks to run at different intervals
    # For hourly task, use every() with hours=1

    # Works 
    # schedule.every(1).hours.do(deleteFilesExceptLatest('C:\path\somewhere', 'keyword', '.txt'))
    # ('1', 'minute', deleteFilesExceptLatest, cleanDir, pattern, ext)
    # schedule.every(1).minutes.do(deleteFilesExceptLatest(cleanDir, pattern, ext))
    # schedule.every(1).minutes.do(deleteFilesByPattern(cleanDir, pattern, ext))

    # For a task every 12 hours, use every() with hours=12
    # schedule.every(12).hours.do(deleteFilesByPattern(cleanDir, pattern, ext))

    schedule_tasks()
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
