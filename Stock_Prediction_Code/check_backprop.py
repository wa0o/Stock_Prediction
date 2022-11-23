import tkinter as tk
from jpg import backprop_jpg1, backprop_jpg2, backprop_jpg3


def bp_jpg1():
    backprop_jpg1.child_screen()


def bp_jpg2():
    backprop_jpg2.child_screen()


def bp_jpg3():
    backprop_jpg3.child_screen()


def quit_():
    tk.Tk().quit()


def child_screen():
    root = tk.Tk()
    root.title("我的网络")
    root.geometry("400x350+200+100")

    label = tk.Label(root, text="请选择想查看的代码片段：", font=('幼圆', 12))
    label.place(x=40, y=10)
    b1 = tk.Button(root, text="node_update", command=bp_jpg1,  width=15, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b1.place(x=40, y=60)
    b2 = tk.Button(root, text="error_update", command=bp_jpg2,  width=15, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b2.place(x=40, y=110)
    b3 = tk.Button(root, text="weight_update", command=bp_jpg3,  width=15, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b3.place(x=40, y=160)

    # b = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    # b.place(x=285, y=280)
