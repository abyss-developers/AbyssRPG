import pyautogui
script = "e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e"

for x in script.split():
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("https://www.youtube.com/watch?v=mPVDGOVjRQ0")
    pyautogui.press("enter")

#pyautogui.press("up")
#pyautogui.hotkey("ctrl", "a")
#pyautogui.press("delete")
#pyautogui.press("enter")
#pyautogui.press("enter")
