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
permitted = False
not_permitted = False

def no_clicked(event):
    if permitted and not not_permitted:
        headline.destroy()
        no_button.destroy()
        yes_button.destroy()
        Label(root, text="Good for you.", font=("Arial", "15")).place(x=150, y=50, anchor=CENTER)
    else:
        no_enter(event)


def no_enter(event):
    global not_permitted
    if permitted and not not_permitted:
        return
    global entered
    not_permitted = True
    entered = True
    while entered:
        x = randint(25, 225)
        if x > 125:
            y = randint(25, 75)
        else:
            y = randint(25, 175)
        no_button.place(x=x, y=y, height=50, width=50)
        root.update()

def no_leave(event):
    global entered
    entered = False

no_button.bind("<Button-1>", no_clicked)
no_button.bind("<Enter>", no_enter)
no_button.bind("<Leave>", no_leave)


def yes_clicked(event):
    headline.destroy()
    no_button.destroy()
    yes_button.destroy()
    Label(root, text="I knew it!", font=("Arial", "15")).place(x=150, y=50, anchor=CENTER)

def yes_enter(event):
    global permitted
    permitted = True

yes_button.bind("<Button-1>", yes_clicked)
yes_button.bind("<Enter>", yes_enter)

headline.place(x=150, y=50, anchor=CENTER)
no_button.place(x=50, y=150, height=50, width=50)
yes_button.place(x=200, y=150, height=50, width=50)
root.mainloop()

