import tkinter as tk
from PIL import Image, ImageTk


def quit_():
    tk.Tk().quit()


def child_screen():
    font = r'C:\Users\TREE\Desktop\整合\SIMYOU.ttf'

    root = tk.Toplevel()
    root.title("我的网络")
    root.geometry("400x350+200+100")

    image = Image.open("stock.JPG").resize((400, 350))
    global image_
    image_ = ImageTk.PhotoImage(image)
    label_image = tk.Label(root, image=image_)
    label_image.grid(row=0, column=0)

    b_ = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    b_.place(x=285, y=280)
