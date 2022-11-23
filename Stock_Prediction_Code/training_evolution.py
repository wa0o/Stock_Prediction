import tkinter as tk
from ea import ea
import check_EA


def train():  # 开始训练（（（接口）））
    ea.ea_experiment()


def check():
    check_EA.child_screen()


def quit_():
    tk.Tk().quit()


def child_screen():
    root = tk.Tk()
    root.title("我的网络")
    root.geometry("400x350+200+100")

    b1 = tk.Button(root, text='开始训练', command=train, width=10, height=2, font=('幼圆', 12))
    b1.place(x=150, y=115)
    b2 = tk.Button(root, text='查看原代码', command=check, width=10, height=2, font=('幼圆', 12))
    b2.place(x=150, y=165)

    b = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    b.place(x=285, y=280)
