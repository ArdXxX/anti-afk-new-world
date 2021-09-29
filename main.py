import pyautogui
from win32gui import GetWindowText, GetForegroundWindow
import win32gui
import time
import random

windowName = 'New World'
hwnd = win32gui.FindWindowEx(0,0,0, windowName)
keys = ['a', 'd', 'w', 's', 'space']

print('Initializing New World -ANTI AFK-')

def main():
    while True:
        if win32gui.FindWindow(None, windowName): 
            currentWindow = GetWindowText(GetForegroundWindow())
            if(currentWindow == windowName):
                key = random.randint(0, 4)
                pyautogui.press(keys[key])
                print('NW Anti AFK, sending key : ' + keys[key])    
            else:
                win32gui.SetForegroundWindow(hwnd)
                print('Bringing NW window to front')
                time.sleep(2)
                continue
                    
            r = random.randint(1, 300)
            print('Waiting ' + str(r) + ' seconds to repeat')
            time.sleep(r)
        else:
            print('New World not found, terminating')
            break
    
if __name__ == "__main__":
    main()
