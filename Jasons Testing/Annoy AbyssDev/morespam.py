import pyautogui

e = 0

while True:
    if e >= 20:
        pyautogui.write("The machine has exceeded 20 reminders. I shall now break.")
        break
    pyautogui.write("**Water Rehydration Reminder**")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("This message is automatically sent by Jason's code to remind you that you need to stay hydrated.")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("This message will sent in 5 more minutes.")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("Have a nice day!", interval=20)
    pyautogui.press("enter")
    e += 1    
    