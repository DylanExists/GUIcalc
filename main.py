from tkinter import *
from functools import partial
root = Tk()

# setup variable section
varx = StringVar(root, value="0") # varx = output box variable
strx = varx.get() # strx = varx but in string
owt = 0
# setup variable section

# setup window section
root.title("GUIcalc BETA") # window title
root.iconphoto(False, PhotoImage(file="windowicon.png")) # window icon
frame = Frame(root, width=250, height=125).pack() # window frame size
root.resizable(0, 0) # window resizability (false)
# setup window section

# label section
label1 = Label(root, textvariable=varx, width=32, borderwidth=5, relief="sunken", anchor=E)
label1.place(x=8, y=10) # label1 = output box
# label section

# functions section
def numBut(num):
    global varx
    global owt
    out = int(strx) + num + owt
    if len(str(out)) == 38:
        out = str(out)[:37]
        return
    owt = out * 10
    varx.set(out)
# functions section

# number button section
button1 = Button(root, text="1", command=partial(numBut, 1)).place(x=8, y=40) # "1" button
button2 = Button(root, text="2", command=partial(numBut, 2)).place(x=28, y=40) # "2" button
button3 = Button(root, text="3", command=partial(numBut, 3)).place(x=48, y=40) # "3" button
button4 = Button(root, text="4", command=partial(numBut, 4)).place(x=8, y=68) # "4" button
button5 = Button(root, text="5", command=partial(numBut, 5)).place(x=28, y=68) # "5" button
button6 = Button(root, text="6", command=partial(numBut, 6)).place(x=48, y=68) # "6" button
button7 = Button(root, text="7", command=partial(numBut, 7)).place(x=8, y=96) # "7" button
button8 = Button(root, text="8", command=partial(numBut, 8)).place(x=28, y=96) # "8" button
button9 = Button(root, text="9", command=partial(numBut, 9)).place(x=48, y=96) # "9" button
button10 = Button(root, text="0", height=4, command=partial(numBut, 0)).place(x=68, y=46) # "0" button
# number button section

# operation button section
button11 = Button(root, text="+", width=1).place(x=88, y=40) # addition
button12 = Button(root, text="-", width=1).place(x=108, y=40) # subtraction
button13 = Button(root, text="x", width=1).place(x=88, y=68) # multiplication
button14 = Button(root, text="^", width=1).place(x=108, y=68) # exponentation
button15 = Button(root, text="/", width=1).place(x=88, y=96) # perfect division
button16 = Button(root, text="//", width=1).place(x=108, y=96) # division with remainder
button17 = Button(root, text="=", width=1, height=4).place(x=128, y=46) # equal
# operation button section

root.mainloop()