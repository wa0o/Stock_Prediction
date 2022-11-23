import tkinter as tk
import training_gradient_descent
from backprop import net_params
from backprop import backprop
import check_backprop
from jpg import backprop_jpg1, backprop_jpg2, backprop_jpg3

p = net_params.net_params()


def train():  # 开始训练（（（接口）））
    backprop.backprop_experiment()


# def check():
#     check_backprop.child_screen()


def bp_jpg1():
    backprop_jpg1.child_screen()


def bp_jpg2():
    backprop_jpg2.child_screen()


def bp_jpg3():
    backprop_jpg3.child_screen()


def quit_():
    tk.Tk().quit()


def child_screen():
    font = r'C:\Users\TREE\Desktop\整合\SIMYOU.ttf'
    font = r'C:\Users\TREE\Desktop\整合\CascadiaCode.ttf'

    root = tk.Tk()
    root.title("反向传播算法")
    root.geometry("800x400+200+100")

    label = tk.Label(root, text="请设置参数：", font=('幼圆', 12))
    label.place(x=40, y=10)
    label1 = tk.Label(root, text="input_size:", font=('Cascadia Code ExtraLight', 10))
    label1.place(x=40, y=40)
    label2 = tk.Label(root, text="hidden0:", font=('Cascadia Code ExtraLight', 10))
    label2.place(x=40, y=80)
    label3 = tk.Label(root, text="hidden1:", font=('Cascadia Code ExtraLight', 10))
    label3.place(x=40, y=120)
    label4 = tk.Label(root, text="learning_rate:", font=('Cascadia Code ExtraLight', 10))
    label4.place(x=40, y=160)
    label5 = tk.Label(root, text="learning_decat:", font=('Cascadia Code ExtraLight', 10))
    label5.place(x=40, y=200)
    label6 = tk.Label(root, text="gen_num:", font=('Cascadia Code ExtraLight', 10))
    label6.place(x=40, y=240)

    label7 = tk.Label(root, text="default : 4 (输入结点的数量)", font=('Baskerville Old Face', 10))
    label7.place(x=40, y=60)
    label8 = tk.Label(root, text="default : 50 (隐藏层0的大小)", font=('Baskerville Old Face', 10))
    label8.place(x=40, y=100)
    label9 = tk.Label(root, text="default : 20 (隐藏层1的大小)", font=('Baskerville Old Face', 10))
    label9.place(x=40, y=140)
    label10 = tk.Label(root, text="default : 0.1 (学习率)", font=('Baskerville Old Face', 10))
    label10.place(x=40, y=180)
    label11 = tk.Label(root, text="default : 0.1 (学习的削减程度)", font=('Baskerville Old Face', 10))
    label11.place(x=40, y=220)
    label12 = tk.Label(root, text="default : 10000 (迭代次数)", font=('Baskerville Old Face', 10))
    label12.place(x=40, y=260)

    text1 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text1.place(x=220, y=45)
    text2 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text2.place(x=220, y=85)
    text3 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text3.place(x=220, y=125)
    text4 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text4.place(x=220, y=165)
    text5 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text5.place(x=220, y=205)
    text6 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text6.place(x=220, y=245)

    def get_weight1():
        weight1 = text1.get("1.0", "end-1c")  # weight-权重，用于预测的网络参数
        if weight1 == '':
            weight1 = 4
        return weight1

    def get_weight2():
        weight2 = text2.get("1.0", "end-1c")
        if weight2 == '':
            weight2 = 50
        return weight2

    def get_weight3():
        weight3 = text3.get("1.0", "end-1c")
        if weight3 == '':
            weight3 = 20
        return weight3

    def get_weight4():
        weight4 = text4.get("1.0", "end-1c")
        if weight4 == '':
            weight4 = 0.1
        return weight4

    def get_weight5():
        weight5 = text5.get("1.0", "end-1c")
        if weight5 == '':
            weight5 = 0.1
        return weight5

    def get_weight6():
        weight6 = text6.get("1.0", "end-1c")
        if weight6 == '':
            weight6 = 10000
        return weight6

    def next_page_jump():
        training_gradient_descent.child_screen()

    def next_page():
        p.get_input_size(get_weight1())
        p.get_hidden0(get_weight2())
        p.get_hidden1(get_weight3())
        p.get_learing_rate(get_weight4())
        p.get_learing_decat(get_weight5())
        p.get_gen_num(get_weight6())

        # training_gradient_descent.child_screen()

    b1 = tk.Button(root, text='使用默认参数', width=15, height=2, font=('幼圆', 12))
    b1.place(x=220, y=285)
    b2 = tk.Button(root, text='确认', command=next_page, width=15, height=2, font=('幼圆', 12))
    b2.place(x=220, y=335)
    b3 = tk.Button(root, text='开始训练', command=train, width=15, height=2, font=('幼圆', 12))
    b3.place(x=535, y=285)
    # b4 = tk.Button(root, text='查看原代码', command=check, width=15, height=2, font=('幼圆', 12))
    # b4.place(x=535, y=295)
    # b_ = tk.Button(root, text='退出', command=quit_, width=15, height=2, font=('幼圆', 12))
    # b_.place(x=660, y=550)

    label = tk.Label(root, text="请选择想查看的代码片段：", font=('幼圆', 12))
    label.place(x=440, y=10)
    b1 = tk.Button(root, text="node_update", command=bp_jpg1, width=15, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b1.place(x=440, y=60)
    b2 = tk.Button(root, text="error_update", command=bp_jpg2, width=15, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b2.place(x=440, y=110)
    b3 = tk.Button(root, text="weight_update", command=bp_jpg3, width=15, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b3.place(x=440, y=160)
