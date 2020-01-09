from algorithm import *
import tkinter as tk
from tkinter import *

def encode():
    ed.delete('1.0', END)
    ed.insert('1.0', encrypt(ee.get("1.0",'end-1c')))
    return

def decode():
    ee.delete('1.0', END)
    ee.insert('1.0', decrypt(ed.get("1.0",'end-1c')))
    return

window = tk.Tk() 
window.title("RSA")
window.minsize(1000, 500)

Label(window, text = "Plain Text").grid(row = 0, column = 0)
ee = Text(window, height = 5, width = 100)
ee.grid(row = 0, column = 1)

Label(window, text = "Cipher Text").grid(row = 1, column = 0)
ed = Text(window, height = 5, width = 100)
ed.grid(row = 1, column = 1)

button1 = tk.Button(window, text = 'Encrypt', command = lambda: encode(), height = 10, width = 20)
button1.grid(row = 2, column = 0)

button2 = tk.Button(window, text = 'Decrypt', command = lambda: decode(), height = 10, width = 20)
button2.grid(row = 2, column = 1)

window.mainloop()