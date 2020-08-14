from tkinter import *
root = Tk()

# setup variable section
x = 0000000000000000000000000000000000000 # x = output box variable
x = str(x)[:37]    # maximum characters ^
# setup variable section

# setup window section
root.title("GUIcalc") # window title
root.iconphoto(False, PhotoImage(file="windowicon.png")) # window icon
frame = Frame(root, width=250, height=125).pack() # window frame size
root.resizable(0, 0) # window resizability (false)
# setup window section

# label section
label1 = Label(root, text=str(x), width=32, borderwidth=5, relief="sunken", anchor=E)
label1.place(x=8, y=10) # label1 = output box
# label section

# number button section
button1 = Button(root, text="1").place(x=8, y=40) # "1" button
button2 = Button(root, text="2").place(x=28, y=40) # "2" button
button3 = Button(root, text="3").place(x=48, y=40) # "3" button
button4 = Button(root, text="4").place(x=8, y=68) # "4" button
button5 = Button(root, text="5").place(x=28, y=68) # "5" button
button6 = Button(root, text="6").place(x=48, y=68) # "6" button
button7 = Button(root, text="7").place(x=8, y=96) # "7" button
button8 = Button(root, text="8").place(x=28, y=96) # "8" button
button9 = Button(root, text="9").place(x=48, y=96) # "9" button
button10 = Button(root, text="0", height=4).place(x=68, y=46) # "0" button
# number button section

root.mainloop()