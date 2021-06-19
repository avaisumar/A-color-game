from tkinter import *
import random

root = Tk()
root.title("COLOR GAME")
root.geometry("275x300")

timeleft = 30
scr=0
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']


def count():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        time.config(text="time left:--" + str(timeleft))
        time.after(1000, count)


def nextclr():
    global scr
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
            scr += 1

        # clear the text entry box.
        e.delete(0, END)

        random.shuffle(colours)

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        dl.config(fg=str(colours[1]), text=str(colours[0]))

        # update the score.
        score.config(text="Score: " + str(scr))


def strt(event):
    if timeleft == 30:
        count()
    nextclr()


# labels
ins = Label(root, text="type the color of text not text", font=('helvetica', 12))
ins.pack()
score = Label(root, text="enter to start", font=('helvetica', 12))
score.pack()
time = Label(root, text="time left:--" + str(timeleft), font=('helvetica', 12))
time.pack()
dl = Label(root, font=('helvetica', 60))
dl.pack()
e = Entry(root)
root.bind('<Return>', strt)
e.pack()
e.focus_set()
root.mainloop()
