# 排程, 函式, 資料夾, 路徑, 檔名, 關鍵字, 間隔, 年月日, 時分, 指定時間
import glob
import os
import time
import datetime
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
def schedule_tasks():
    # for interval, unit, func, *args in tasks:
    #     if unit == 'hour':
    #         schedule.every(interval).hours.do(func, *args)
    #     elif unit == 'minutes':
    #         schedule.every(interval).minutes.do(func, *args)
    current_time = datetime.datetime.now()
    # print(f"current time: {current_time}")
    for item in tasks:
        if isinstance(item[0], int):  # Interval-based task
            interval, unit, func, *args = item
            if unit == 'year':
                # Schedule yearly tasks by setting them to run on a specific date each year
                scheduled_time = current_time.replace(year=current_time.year + interval)
                schedule.every().day.at(scheduled_time.strftime('%H:%M:%S')).do(func, *args)
            elif unit == 'month':
                # Schedule monthly tasks by setting them to run on a specific date each month
                scheduled_time = current_time.replace(month=current_time.month + interval)
                schedule.every().day.at(scheduled_time.strftime('%H:%M:%S')).do(func, *args)
            elif unit == 'day':
                schedule.every(interval).days.do(func, *args)
            elif unit == 'hour':
                schedule.every(interval).hours.do(func, *args)
            elif unit == 'minute':
                schedule.every(interval).minutes.do(func, *args)
            print(f"current time: {current_time}")
        elif item[1] == 'at' and current_time.strftime('%H:%M:%S') == item[0]:  # Time-based task
            _, _, func, *args = item
            func(*args)
            print(f"current time: {current_time}")

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
