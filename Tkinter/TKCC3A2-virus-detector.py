from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Virus Detector")
window.geometry("400x100")

def show_msg():
    messagebox.showwarning("Virus scanner","Stop Virus detected")

button = Button(window, text="Scan", command=show_msg)
button.place(x=40, y=80)

window.mainloop()



