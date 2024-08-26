from tkinter import *
from datetime import date

window = Tk()
window.title("Simple Input box")
window.geometry('400x300')

# add labels
lbl_head = Label(text="Hey there!", fg="white" , bg="darkgray" , height=1, width=300)    
lbl_name = Label(text="Full name" , bg="#3CBEC4")
entry_name = Entry()


def display():
    first_name = entry_name.get()
    global message
    message = "Welcome to your application!\nTodays date is:"
    greet = f"Hello!{first_name.capitalize()}"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())


text_box = Text(height = 3)
btn_disp = Button(text = "Begin" , command=display, height=1, bg="#3CBEC4", fg="white")

lbl_head.pack()
lbl_name.pack()
entry_name.pack()
btn_disp.pack()
text_box.pack()





window.mainloop()