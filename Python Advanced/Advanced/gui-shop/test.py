import tkinter as tk
from PIL import Image,ImageTk
window=tk.Tk()
tk.Label(text='Na maika ti v gyza').grid(row=1,column=0)
window.geometry("700x700")

image=ImageTk.PhotoImage(Image.open("./data_base/images/laptop.jpg").resize((100,100)))
tk.Label(window,image=image).grid(row=3,column=3)

window.mainloop()