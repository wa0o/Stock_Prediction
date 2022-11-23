import tkinter as tk
import read_sin
import read_dataset


def gradient_des_sin():
    read_sin.show_one(1)


def evo_sin():
    read_sin.show_one(3)


def evo_dynamic_sample_sin():
    read_sin.show_one(7)


def limit_evo_single_sin():
    read_sin.show_one(4)


def limit_evo_elitist_sin():
    read_sin.show_one(5)


def limit_evo_inherit_sin():
    read_sin.show_one(6)


def gradient_des_dataset():
    read_dataset.show_one(1)


def evo_dataset():
    read_dataset.show_one(3)


def evo_dynamic_sample_dataset():
    read_dataset.show_one(7)


def limit_evo_single_dataset():
    read_dataset.show_one(4)


def limit_evo_elitist_dataset():
    read_dataset.show_one(5)


def limit_evo_inherit_dataset():
    read_dataset.show_one(6)


def compare_all_sin():
    read_sin.showpart1()


def compare_leea_sin():
    read_sin.showpart2()


def compare_all_dataset():
    read_dataset.showpart1()


def compare_leea_dataset():
    read_dataset.showpart2()


def quit_():
    tk.Tk().quit()


def child_screen():
    font = r'C:\Users\TREE\Desktop\整合\SIMYOU.ttf'

    root = tk.Tk()
    root.title("算法性能比较展示")
    root.geometry("800x350+200+100")

    label1 = tk.Label(root, text="SIN函数的拟合：", font=('幼圆', 12))
    label1.place(x=40, y=10)
    label2 = tk.Label(root, text="数据集的拟合：", font=('幼圆', 12))
    label2.place(x=440, y=10)
    label3 = tk.Label(root, text="性能比较：", font=('幼圆', 12))
    label3.place(x=40, y=215)
    label4 = tk.Label(root, text="性能比较：", font=('幼圆', 12))
    label4.place(x=440, y=215)

    b1 = tk.Button(root, text='反向传播', command=gradient_des_sin, width=15, height=2, font=('幼圆', 12))
    b1.place(x=55, y=35)
    b2 = tk.Button(root, text='进化', command=evo_sin, width=15, height=2, font=('幼圆', 12))
    b2.place(x=55, y=85)
    b3 = tk.Button(root, text='进化(部分样本)', command=evo_dynamic_sample_sin, width=15, height=2, font=('幼圆', 12))
    b3.place(x=55, y=135)
    b4 = tk.Button(root, text='有限进化', command=limit_evo_single_sin, width=15, height=2, font=('幼圆', 12))
    b4.place(x=205, y=35)
    # b5 = tk.Button(root, text='有限进化(多进程)', command=limit_evo, width=15, height=2, font=('幼圆', 12))
    # b5.place(x=590, y=35)
    b6 = tk.Button(root, text='有限进化(精英)', command=limit_evo_elitist_sin, width=15, height=2, font=('幼圆', 12))
    b6.place(x=205, y=85)
    b7 = tk.Button(root, text='有限进化(继承)', command=limit_evo_inherit_sin, width=15, height=2, font=('幼圆', 12))
    b7.place(x=205, y=135)
    # b8 = tk.Button(root, text='算法性能比较', command=comp, width=15, height=2, font=('幼圆', 12))
    # b8.place(x=590, y=185)

    b9 = tk.Button(root, text='反向传播', command=gradient_des_dataset, width=15, height=2, font=('幼圆', 12))
    b9.place(x=455, y=35)
    b10 = tk.Button(root, text='进化', command=evo_dataset, width=15, height=2, font=('幼圆', 12))
    b10.place(x=455, y=85)
    b11 = tk.Button(root, text='进化(部分样本)', command=evo_dynamic_sample_dataset, width=15, height=2, font=('幼圆', 12))
    b11.place(x=455, y=135)
    b12 = tk.Button(root, text='有限进化', command=limit_evo_single_dataset, width=15, height=2, font=('幼圆', 12))
    b12.place(x=605, y=35)
    b13 = tk.Button(root, text='有限进化(精英)', command=limit_evo_elitist_dataset, width=15, height=2, font=('幼圆', 12))
    b13.place(x=605, y=85)
    b14 = tk.Button(root, text='有限进化(继承)', command=limit_evo_inherit_dataset, width=15, height=2, font=('幼圆', 12))
    b14.place(x=605, y=135)

    b15 = tk.Button(root, text='不同算法间', command=compare_all_sin, width=15, height=2, font=('幼圆', 12))
    b15.place(x=55, y=240)
    b16 = tk.Button(root, text='LEEA算法变体间', command=compare_leea_sin, width=15, height=2, font=('幼圆', 12))
    b16.place(x=205, y=240)
    b17 = tk.Button(root, text='不同算法间', command=compare_all_dataset, width=15, height=2, font=('幼圆', 12))
    b17.place(x=455, y=240)
    b18 = tk.Button(root, text='LEEA算法变体间', command=compare_leea_dataset, width=15, height=2, font=('幼圆', 12))
    b18.place(x=605, y=240)

    # b = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    # b.place(x=285, y=280)
