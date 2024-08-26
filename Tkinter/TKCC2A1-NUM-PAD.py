from tkinter import *


root = Tk()
root.title("Number Pad")

root.geometry("250x300")

numes = [["9","8","7"],["6","5","4"],["3","2","1"],["#","0","*"]]


frame1 = Frame(master=root)
frame1.pack(fill=BOTH)


button_width = 10
button_height = 3

for i in range(4):
    for j in range(3):
        button = Button(
            master=frame1,
            text=numes[i][j],
            bg="white",
            fg="black",
            width=button_width,
            height=button_height,
        )
        button.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
        
for i in range(4):
    frame1.grid_rowconfigure(1, weight=1)
for j in range(3):
    frame1.grid_columnconfigure(j, weight=1)


root.mainloop()