import pyautogui
script = "BYE BYE BYE BYE BYE BYE BYE BYE BYE BYE BYE BYE BYE BYE BYE "

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")