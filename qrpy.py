import tkinter as tk
from tkinter import *
import re
import pyqrcode
from PIL import Image,ImageTk
top = tk.Tk()
top.geometry("500x500")
top.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
top.resizable(0, 0)
canvas1 = tk.Canvas(top, width = 400, height = 300)
canvas1.pack()
s_var = tk.Entry(top)
canvas1.create_window(200, 100, window=s_var)

password_entry = tk.Entry(top, show="*")
canvas1.create_window(200, 170, window=password_entry)
def password():
    s = s_var.get()
    pwd = re.findall(r'\b([a-zA-Z]|\d+)', s)
    pwd = "".join(pwd)
    passwrd = password_entry.get()

    if passwrd == pwd:
        img_lbl.config(image=img)
        output.config(text="QR code ")
    else :
        w = tk.Label(top, text='error', font="50")
        w.pack()
        msg = tk.Message(top, text="please enter correct password")
        msg.pack()

def getqrcode():
    global qr,img
    p = s_var.get()
    qr = pyqrcode.create(p)
    img = BitmapImage(data=qr.xbm(scale=8))
    #qr.save('my_qrcode.png')
button1 = tk.Button(text='Generate qr code', command=getqrcode)
canvas1.create_window(200, 140, window=button1)
button2 = tk.Button(text='submit', command=password)
canvas1.create_window(200, 200, window=button2)
img_lbl = tk.Label(top)
img_lbl.pack()
output = tk.Label(top,text="output")
output.pack()
top.mainloop()