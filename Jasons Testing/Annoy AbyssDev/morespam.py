import pyautogui
import pygame

while True:
    pyautogui.write("**Water Rehydration Reminder**")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("> This message is automatically sent by Jason's code to remind you that you need to stay hydrated.")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("> This message will sent in 10 more minutes.")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write("> Have a nice day!")
    pyautogui.press("enter", interval=600)