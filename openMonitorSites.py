# 開啟4個 Firefox 視窗、連到4個指定的網站、用視窗名稱的關鍵字將視窗移到4個角落形成4分割
import os
import pyautogui
import time
import pygetwindow as gw
from screeninfo import get_monitors

# Function to check if a Firefox window with a specific title keyword exists and open a new one if not
def open_firefox_window(url, title_keyword):
    # Search for Firefox windows with a specific title keyword
    firefox_windows = [window for window in gw.getAllTitles() if title_keyword in window]

    if firefox_windows:
        # If a Firefox window with the title keyword exists, use it
        opened_window = gw.getWindowsWithTitle(firefox_windows[0])[0]
    else:
        # If not, open a new Firefox window with the URL
        os.system(f'start firefox -new-window {url}')
        # Wait for the browser to open (adjust sleep duration as needed)
        time.sleep(2)

        # Find the newly opened Firefox window
        opened_window = gw.getWindowsWithTitle("Mozilla Firefox")[0]

    if opened_window is None or "頁面載入發生問題" in opened_window.title:
        # Break the loop if the window is not found or contains the specific title
        return None

    opened_window.resizeTo(window_width, window_height)
    return opened_window

# List of websites to visit
monitorSites = ["url1", "url2", "url3", "url4"]
siteTitle = ["keyword1", "keyword2", "keyword3", "keyword4"]
taskbarH = 50
# Get the second monitor (monitor 1, as the list is 0-indexed)
second_monitor = get_monitors()[0]

# Calculate the window width and height (50% of the monitor's resolution)
window_width = second_monitor.width // 2
window_height = (second_monitor.height -taskbarH) // 2

# Calculate window positions at the four corners
window_positions = [
    (second_monitor.x, second_monitor.y),                                     # Top left corner
    (second_monitor.x + window_width, second_monitor.y),                     # Top right corner
    (second_monitor.x, second_monitor.y + window_height),                     # Bottom left corner
    (second_monitor.x + window_width, second_monitor.y + window_height)      # Bottom right corner
]

# Flag to control whether to continue running the script
should_run = True

for i, url in enumerate(monitorSites):
    if should_run:
        title_keyword = siteTitle[i]
        opened_window = open_firefox_window(url, title_keyword)

        if opened_window is None:
            should_run = False  # Stop running the script if a window is not found or has specific title
        opened_window.moveTo(window_positions[i][0], window_positions[i][1])

# The script will continue running as long as should_run is True and will stop when should_run becomes False.
