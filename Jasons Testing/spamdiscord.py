import pyautogui
script = "hello"

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")