import tkinter as tk
from caeserCipher import *
from tkinter import *
from tkinter.messagebox import showinfo

def encode():
    if validatePlaintext(ep.get()) == False:
        showinfo("Warning", "The plaintext should contain only lower case letters & spaces")
        return
    if ek.get().isdecimal() == False or int(ek.get()) < 0:
        showinfo("Warning", "The key should be a positive number")
        return
    ec.delete(0, END)
    ec.insert(0, encodeText(ep.get(), int(ek.get())))
    return

def decode():
    if validateCiphertext(ec.get()) == False:
        showinfo("Warning", "The ciphertext should contain only upper case letters & spaces")
        return
    if ek.get().isdecimal() == False or int(ek.get()) < 0:
        tk.messagebox("Warning", "The key should be a positive number")
        return
    ep.delete(0, END)
    ep.insert(0, decodeText(ec.get(), int(ek.get())))
    return

window = tk.Tk() 
window.title("Caeser Cipher")
window.minsize(250, 200)

Label(window, text = "Plain Text").pack()
ep = Entry(window)
ep.pack()

Label(window, text = "Key").pack()
ek = Entry(window)
ek.pack()

Label(window, text = "Cipher Text").pack()
ec = Entry(window)
ec.pack()

button = tk.Button(window, text = 'Encrypt', command = lambda: encode())
button.pack()

button = tk.Button(window, text = 'Decrypt', command = lambda: decode())
button.pack()

window.mainloop()