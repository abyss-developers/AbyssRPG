import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = 0.25  # in seconds
resume_key = Key.left
pause_key = Key.right
exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pyautogui.press("delete")
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pyautogui.press("delete")
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// Jason's Discord Deleter")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Left Arrow Key")
    print("\t F2 = Right Arrow Key")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.press("up")
            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("delete")
            pyautogui.press("enter")
            pyautogui.click(x=1117, y=615)
            pyautogui.click(x=455, y=1011)
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
