import pyautogui
import keyboard
polygonX = 511
polygonY = 266
markerX = 511
markerY = 320
def polygon():
    startX, startY = pyautogui.position()
    pyautogui.moveTo(polygonX, polygonY)
    pyautogui.leftClick()
    pyautogui.moveTo(startX, startY)
def marker():
    startX, startY = pyautogui.position()
    pyautogui.moveTo(markerX, markerY)
    pyautogui.leftClick()
    pyautogui.moveTo(startX, startY)

def hotkeys():
    loop = True
    while loop:
        if keyboard.is_pressed('alt+m'):
            marker()
        if keyboard.is_pressed('alt+n'):
            polygon()
        if keyboard.is_pressed('alt+q'):
            loop = False

 hotkeys()
