import pyautogui

while True:
    pyautogui.write("**Hello**")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("> This is Jason's attempt at automating talking so he doesn't have to talk to people")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("> This message was completely automated and Jason didn't have to send anything")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("> And also please @ me for things you need by the real jason!!")
    pyautogui.press("enter", interval=1)