import tkinter as tk
import gradient_descent
import evolution
import evolution_dynamic_sample
import limit_evolution_single
import limit_evolution
import limit_evolution_elitist
import limit_evolution_inherit


def gradient_des():
    gradient_descent.child_screen()


def evo():
    evolution.child_screen()


def evo_dynamic_sample():
    evolution_dynamic_sample.child_screen()


def limit_evo_single():
    limit_evolution_single.child_screen()


def limit_evo():
    limit_evolution.child_screen()


def limit_evo_elitist():
    limit_evolution_elitist.child_screen()


def limit_evo_inherit():
    limit_evolution_inherit.child_screen()


def quit_():
    tk.Tk().quit()


def child_screen():
    root = tk.Tk()
    root.title("我的网络")
    root.geometry("400x350+200+100")

    label = tk.Label(root, text="请选择训练方式：", font=('幼圆', 12))
    label.place(x=40, y=10)

    b1 = tk.Button(root, text='反向传播', command=gradient_des, width=15, height=2, font=('幼圆', 12))
    b1.place(x=40, y=35)
    b2 = tk.Button(root, text='进化', command=evo, width=15, height=2, font=('幼圆', 12))
    b2.place(x=40, y=85)
    b3 = tk.Button(root, text='进化(部分样本)', command=evo_dynamic_sample, width=15, height=2, font=('幼圆', 12))
    b3.place(x=40, y=135)
    b4 = tk.Button(root, text='有限进化', command=limit_evo_single, width=15, height=2, font=('幼圆', 12))
    b4.place(x=40, y=185)
    b5 = tk.Button(root, text='有限进化(多进程)', command=limit_evo, width=15, height=2, font=('幼圆', 12))
    b5.place(x=190, y=35)
    b6 = tk.Button(root, text='有限进化(精英)', command=limit_evo_elitist, width=15, height=2, font=('幼圆', 12))
    b6.place(x=190, y=85)
    b7 = tk.Button(root, text='有限进化(继承)', command=limit_evo_inherit, width=15, height=2, font=('幼圆', 12))
    b7.place(x=190, y=135)

    b = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    b.place(x=285, y=280)
