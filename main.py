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

root.mainloop()