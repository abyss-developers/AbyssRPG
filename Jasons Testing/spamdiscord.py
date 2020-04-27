import pyautogui
script = "WOULD YOU LIKE ME TO STOP"

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")

#pyautogui.press("up")
#pyautogui.hotkey("ctrl", "a")
#pyautogui.press("delete")
#pyautogui.press("enter")
#pyautogui.press("enter")
