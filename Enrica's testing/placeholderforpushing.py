import pyautogui
script = "goodnight goodnight I am smol child of the underworld but I have good friend Jasoni"

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")
