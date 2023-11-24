#.grid() place button on Tk
import tkinter as tk
from screens import render_main_screen

if __name__ == '__main__':
    window=tk.Tk()
    window.geometry('700x700')
    window.title('My gui shop')
    render_main_screen(window)

    window.mainloop()