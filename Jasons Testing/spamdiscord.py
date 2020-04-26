import pyautogui
script = "This might be a stupid question but how do I run HTML or CSS or Javascript code "

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")