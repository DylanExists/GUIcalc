from tkinter import *
root = Tk()
root.title("GUIcalc")
root.iconphoto(False, PhotoImage(file="windowicon.png"))
frame = Frame(root, width=250, height=125).pack()
root.resizable(0, 0)
root.mainloop()