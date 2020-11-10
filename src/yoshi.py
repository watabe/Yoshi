from pynput import mouse
from pynput.mouse import Button
import pyautogui

SCREENSHOT_PREFIX = "yoshi_"
SCREENSHOT_SUFFIX = ".png"

SCREENSHOT_SIZE_WIDTH = 100
SCREENSHOT_SIZE_HEIGHT = 100

screenshot_count = 0

def on_click(x, y, button, pressed):
    global screenshot_count

    if button == Button.middle:
        return False

    if not pressed:
        screenshot = pyautogui.screenshot(region = (
            x-(SCREENSHOT_SIZE_WIDTH/2),
            y-(SCREENSHOT_SIZE_HEIGHT/2),
            SCREENSHOT_SIZE_WIDTH,
            SCREENSHOT_SIZE_HEIGHT))
        screenshot.save(SCREENSHOT_PREFIX +
		    str(screenshot_count).zfill(3) + SCREENSHOT_SUFFIX)

        screenshot_count+=1

with mouse.Listener(
        on_click=on_click,
        ) as listener:
    listener.join()
