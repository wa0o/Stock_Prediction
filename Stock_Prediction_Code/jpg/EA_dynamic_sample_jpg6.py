import tkinter as tk
from PIL import Image, ImageTk


def quit_():
    tk.Tk().quit()


def child_screen():
    font = r'C:\Users\TREE\Desktop\整合\SIMYOU.ttf'
    root = tk.Toplevel()
    root.title("代码片段展示")
    root.geometry("800x550+100+50")

    image = Image.open("jpg\\get_next_generation_EA_dynamic_sample.JPG").resize((800, 300))
    global image_
    image_ = ImageTk.PhotoImage(image)
    label_image = tk.Label(root, image=image_)
    label_image.grid(row=0, column=0)

    # b_ = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    # b_.place(x=650, y=500)
