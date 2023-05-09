# are you dumb?

from tkinter import *
from random import randint

root = Tk()
root.geometry("300x250")
root.resizable(0, 0)


headline = Label(root, text="Are you dumb?", font=("Arial", "15"))
no_button = Button(root, text="No", font=("Arial", "15"))
yes_button = Button(root, text="Yes", font=("Arial", "15"))

entered = False

def no_clicked(event):
    global entered
    entered = True
    while entered:
        x = randint(25, 225)
        if x > 125:
            y = randint(25, 75)
        else:
            y = randint(25, 175)
        no_button.place(x=x, y=y, height=50, width=50)
        root.update()

def no_clicked_leave(event):
    global entered
    entered = False

no_button.bind("<Enter>", no_clicked)
no_button.bind("<Leave>", no_clicked_leave)


def yes_clicked(event):
    headline.destroy()
    no_button.destroy()
    yes_button.destroy()
    Label(root, text="I knew it!", font=("Arial", "15")).place(x=150, y=50, anchor=CENTER)

yes_button.bind("<Button-1>", yes_clicked)

headline.place(x=150, y=50, anchor=CENTER)
no_button.place(x=50, y=150, height=50, width=50)
yes_button.place(x=200, y=150, height=50, width=50)
root.mainloop()

