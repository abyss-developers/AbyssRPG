import pyautogui
script = "I WROTE A PYTHON SCRIPT THAT SPAMS PEOPLE DO YOU HAVE ANYONE IN MIND"

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")

#pyautogui.press("up")
#pyautogui.hotkey("ctrl", "a")
#pyautogui.press("delete")
#pyautogui.press("enter")
#pyautogui.press("enter")
