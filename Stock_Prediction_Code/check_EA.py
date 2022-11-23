import tkinter as tk
from jpg import EA_jpg1, EA_jpg2, EA_jpg3, EA_jpg4, EA_jpg5, EA_jpg6, EA_jpg7, EA_jpg8


def ea_jpg1():
    EA_jpg1.child_screen()


def ea_jpg2():
    EA_jpg2.child_screen()


def ea_jpg3():
    EA_jpg3.child_screen()


def ea_jpg4():
    EA_jpg4.child_screen()


def ea_jpg5():
    EA_jpg5.child_screen()


def ea_jpg6():
    EA_jpg6.child_screen()


def ea_jpg7():
    EA_jpg7.child_screen()


def ea_jpg8():
    EA_jpg8.child_screen()


def quit_():
    tk.Tk().quit()


def child_screen():
    root = tk.Tk()
    root.title("我的网络")
    root.geometry("400x350+200+100")

    label = tk.Label(root, text="请选择想查看的代码片段：", font=('幼圆', 12))
    label.place(x=40, y=10)
    b1 = tk.Button(root, text="node_update", command=ea_jpg1,  width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b1.place(x=40, y=40)
    b2 = tk.Button(root, text="evaluate", command=ea_jpg2,  width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b2.place(x=40, y=70)
    b3 = tk.Button(root, text="get_parent_index", command=ea_jpg3,  width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b3.place(x=40, y=100)
    b4 = tk.Button(root, text="sexual", command=ea_jpg4, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b4.place(x=40, y=130)
    b5 = tk.Button(root, text="asexual", command=ea_jpg5, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b5.place(x=40, y=160)
    b6 = tk.Button(root, text="get_next_generation", command=ea_jpg6, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b6.place(x=40, y=190)
    b7 = tk.Button(root, text="create_first_generation", command=ea_jpg7, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b7.place(x=40, y=220)
    b8 = tk.Button(root, text="produce_offspring", command=ea_jpg8, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b8.place(x=40, y=250)

    # b = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    # b.place(x=285, y=280)
