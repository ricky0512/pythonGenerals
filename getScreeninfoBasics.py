from screeninfo import get_monitors

def get_primary_screen_resolution():
    screen_resolution = pyautogui.size()
    return screen_resolution.width, screen_resolution.height

def get_all_screen_resolutions():
    resolutions = [(monitor.width, monitor.height) for monitor in get_monitors()]
    return resolutions
