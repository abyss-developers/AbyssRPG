import pyautogui
script = "hanging off my earlobe is a rock"

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter", interval=1 )

#pyautogui.press("up")
#pyautogui.hotkey("ctrl", "a")
#pyautogui.press("delete")
#pyautogui.press("enter")
#pyautogui.press("enter")
