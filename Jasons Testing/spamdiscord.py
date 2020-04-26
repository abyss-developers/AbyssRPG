import pyautogui
script = "KELLY I MADE A CODE THINGY WHERE YOU CAN SPAM PEOPLE LMAOOOO WHAT R U DOING RN"

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")