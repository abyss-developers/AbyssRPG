import pyautogui
import pygame
import sys
from tkinter import *

registeredAccounts = [
    "jatgm:199662",
    "ace:spacceghost"
]

pygame.init()
clock = pygame.time.Clock()

root = Tk()
root.title("AnnoyAbyss")
root.geometry("700x600")
root.resizable(0, 0)
root.configure(bg="#f2f2f2")

class actualStuff():
    def __init__(self, body, times):
        self.body = body
        self.times = times
    
    def feature(self):
        return

frame = LabelFrame(root, text="AnnoyAbyss", padx=5, pady=5, font=("sans-serif", 45), bg="#e6e6e6")
frame.pack(padx=10, pady=10, side=TOP)

class newEntrySubmission():
    def __init__(self):
        self.top = Toplevel()
        self.credit = Label(self.top, text="Attribution: Jason Zhou")
        self.SidePanel = Button(self.top, text="Home", width=12, height=100, font=("Ariel", 10),
                        bg="#c4c4c4", state=DISABLED)
        self.HomeButton = Button(self.top, text="Home", width=12, height=15, font=("Ariel", 10),
                        bg="#e6e6e6")
        self.SettingsButton = Button(self.top, text="Options", width=12, height=15, font=("Ariel", 10),
                        bg="#e6e6e6")

        self.clientframe = LabelFrame(self.top, text="Text Entree", padx=2, pady=2, font=("Helvetica", 45))
        self.clientframe.grid(row=1,column=2)

        self.bodyEntree = Entry(self.clientframe, width=80, bg="#e6e6e6", fg="Black", borderwidth=4)
        self.bodyEntree.grid(row=1, column=3, columnspan=2)
        self.bodyEntree.insert(0, "Enter Your Password:")  # Default text
        self.indicator = Label(self.clientframe, text="Input First String Here", bg="#e6e6e6", fg="red")
        self.indicator.grid(row=1, column=2)

        self.bodyEntree1 = Entry(self.clientframe, width=80, bg="#e6e6e6", fg="Black", borderwidth=4)
        self.bodyEntree1.grid(row=2, column=3, columnspan=2)
        self.bodyEntree1.insert(0, "Enter Your Password:")  # Default text
        self.indicator1 = Label(self.clientframe, text="Input Second String Here", bg="#e6e6e6", fg="red")
        self.indicator1.grid(row=2, column=2)

        self.bodyEntree2 = Entry(self.clientframe, width=80, bg="#e6e6e6", fg="Black", borderwidth=4)
        self.bodyEntree2.grid(row=3, column=3, columnspan=2)
        self.bodyEntree2.insert(0, "Enter Your Password:")  # Default text
        self.indicator2 = Label(self.clientframe, text="Input Third String Here", bg="#e6e6e6", fg="red")
        self.indicator2.grid(row=3, column=2)

        self.add = Button(self.clientframe, text="+", font=("Ariel", 10), bg="#0cc935")
        self.add = Button(self.clientframe, text="+", font=("Ariel", 10), bg="#c90c25")
        self.x=4
        self.add.grid(row=self.x,column=1)

        self.SidePanel.grid(row=3, column=1)
        self.HomeButton.grid(row=1, column=1)
        self.SettingsButton.grid(row=2, column=1)

        self.credit.grid(row=4, column=1)
        self.top.geometry("1000x700")
def login():
    checkUser = usernameEntry.get()
    checkPass = passwordEntry.get()
    print("{}:{}".format(checkUser,checkPass))
    for r in registeredAccounts:
        if r == "{}:{}".format(checkUser, checkPass):
            newEntrySubmission()
        else:
            wrongMessage = Label(frame, text="Incorrect username or password!", bg="#e6e6e6", fg="red")
            wrongMessage.grid(row=4, column=1, columnspan=2)
        return

def register():
    NoAccount.destroy()
    myButton.destroy()
    NewButt = Button(frame, text="Register", width=12, height=2, font=("Ariel", 10),
                     bg="#e6e6e6")
    NewButt.grid(row=3, column=2)
    MakeAccount = Button(frame, text="  Have an account?   \n Log in now.", font=("Ariel", 11), bg="#e6e6e6", command=goback)  # command is what it does (Refer to function)
    MakeAccount.grid(row=3, column=1, )
    print("ypo")

def goback():
    NoAccount = Button(frame, text="Don't have an account? \n Sign up now for free.", font=("Ariel", 10), bg="#e6e6e6",
                       command=register)  # command is what it does (Refer to function)
    NoAccount.grid(row=3, column=1)
    myButtone = Button(frame, text="Log In", width=12, height=2, font=("Ariel", 10),
                       bg="#e6e6e6", command=login)
    myButtone.grid(row=3, column=2)
    return

usernameEntry = Entry(frame, width=40, bg="#e6e6e6", fg="Black", borderwidth=4)
usernameEntry.grid(row=1, column=1, columnspan=2)
usernameEntry.insert(0, "Enter Your Username:")  # Default text
passwordEntry = Entry(frame, width=40, bg="#e6e6e6", fg="Black", borderwidth=4)
passwordEntry.grid(row=2, column=1, columnspan=2)
passwordEntry.insert(0, "Enter Your Password:")  # Default text

NoAccount = Button(frame, text="Don't have an account? \n Sign up now for free.", font=("Ariel", 10), bg="#e6e6e6", command=register)  # command is what it does (Refer to function)
NoAccount.grid(row=3, column=1)
myButton = Button(frame, text="Log In", width=12, height=2, font=("Ariel", 10),
                  bg="#e6e6e6", command=login)  # command is what it does (Refer to function)
myButton.grid(row=3, column=2)  # There needs no inside () for functions using commands ^

root.mainloop()

screen_height = 786
screen_width = 1024

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("I am not sorry")

#--Colors for Funz hehehe--#
black = (0, 0, 0)
white = (91, 91, 91)
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
game_font = pygame.font.Font("freesansbold.ttf", 20)

def start_screen():
    while True:

        screen.fill(light_grey)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        clock.tick(60)
        pygame.display.flip()

start_screen()