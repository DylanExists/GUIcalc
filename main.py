from tkinter import *
root = Tk()
x = 0000000000000000000000000000000000000
x = str(x)[:37]    # maximum characters ^
root.title("GUIcalc")
root.iconphoto(False, PhotoImage(file="windowicon.png"))
frame = Frame(root, width=250, height=125).pack()
root.resizable(0, 0)
label1 = Label(root, text=str(x), width=32, borderwidth=5, relief="sunken", anchor=E)
label1.place(x=8, y=10)
root.mainloop()