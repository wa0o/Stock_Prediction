import tkinter as tk
import training_limit_evolution
from leea import net_params
from leea import leea
import check_LEEA
from jpg import LEEA_jpg1, LEEA_jpg2, LEEA_jpg3, LEEA_jpg4, LEEA_jpg5, LEEA_jpg6, LEEA_jpg7, LEEA_jpg8

p = net_params.net_params()


def train():  # 开始训练（（（接口）））
    leea.leea_experiment()


# def check():
#     check_LEEA.child_screen()


def leea_jpg1():
    LEEA_jpg1.child_screen()


def leea_jpg2():
    LEEA_jpg2.child_screen()


def leea_jpg3():
    LEEA_jpg3.child_screen()


def leea_jpg4():
    LEEA_jpg4.child_screen()


def leea_jpg5():
    LEEA_jpg5.child_screen()


def leea_jpg6():
    LEEA_jpg6.child_screen()


def leea_jpg7():
    LEEA_jpg7.child_screen()


def leea_jpg8():
    LEEA_jpg8.child_screen()


def quit_():
    tk.Tk().quit()


def child_screen():
    font = r'C:\Users\TREE\Desktop\整合\SIMYOU.ttf'
    font = r'C:\Users\TREE\Desktop\整合\CascadiaCode.ttf'

    root = tk.Tk()
    root.title("有限进化算法")
    root.geometry("800x600+200+20")

    label = tk.Label(root, text="请设置参数：", font=('幼圆', 12))
    label.place(x=40, y=10)
    label1 = tk.Label(root, text="input_size:", font=('Cascadia Code ExtraLight', 10))
    label1.place(x=40, y=40)
    label2 = tk.Label(root, text="hidden0:", font=('Cascadia Code ExtraLight', 10))
    label2.place(x=40, y=80)
    label3 = tk.Label(root, text="hidden1:", font=('Cascadia Code ExtraLight', 10))
    label3.place(x=40, y=120)
    label4 = tk.Label(root, text="species_size:", font=('Cascadia Code ExtraLight', 10))
    label4.place(x=40, y=160)
    label5 = tk.Label(root, text="parent_num:", font=('Cascadia Code ExtraLight', 10))
    label5.place(x=40, y=200)
    label6 = tk.Label(root, text="ansexual_rate:", font=('Cascadia Code ExtraLight', 10))
    label6.place(x=40, y=240)
    label7 = tk.Label(root, text="fitness_decay:", font=('Cascadia Code ExtraLight', 10))
    label7.place(x=40, y=280)
    label8 = tk.Label(root, text="num_gen:", font=('Cascadia Code ExtraLight', 10))
    label8.place(x=40, y=320)
    label9 = tk.Label(root, text="mutationpower:", font=('Cascadia Code ExtraLight', 10))
    label9.place(x=40, y=360)
    label10 = tk.Label(root, text="mutationpowerdecay:", font=('Cascadia Code ExtraLight', 10))
    label10.place(x=40, y=400)
    label11 = tk.Label(root, text="mutationrate:", font=('Cascadia Code ExtraLight', 10))
    label11.place(x=40, y=440)
    label12 = tk.Label(root, text="mutationratedecay:", font=('Cascadia Code ExtraLight', 10))
    label12.place(x=40, y=480)

    label13 = tk.Label(root, text="default : 5 (输入结点的数量)", font=('Baskerville Old Face', 10))
    label13.place(x=40, y=60)
    label14 = tk.Label(root, text="default : 50 (隐藏层0的大小)", font=('Baskerville Old Face', 10))
    label14.place(x=40, y=100)
    label15 = tk.Label(root, text="default : 20 (隐藏层1的大小)", font=('Baskerville Old Face', 10))
    label15.place(x=40, y=140)
    label16 = tk.Label(root, text="default : 100 (种群大小)", font=('Baskerville Old Face', 10))
    label16.place(x=40, y=180)
    label17 = tk.Label(root, text="default : 40 (选择父母的数量)", font=('Baskerville Old Face', 10))
    label17.place(x=40, y=220)
    label18 = tk.Label(root, text="default : 0.1 (变异的概率)", font=('Baskerville Old Face', 10))
    label18.place(x=40, y=260)
    label19 = tk.Label(root, text="default : 0.2 (适应度的衰减)", font=('Baskerville Old Face', 10))
    label19.place(x=40, y=300)
    label20 = tk.Label(root, text="default : 50 (迭代次数)", font=('Baskerville Old Face', 10))
    label20.place(x=40, y=340)
    label21 = tk.Label(root, text="default : 0.03 (基因突变强度)", font=('Baskerville Old Face', 10))
    label21.place(x=40, y=380)
    label22 = tk.Label(root, text="default : 0.99 (基因突变强度的衰减)", font=('Baskerville Old Face', 10))
    label22.place(x=40, y=420)
    label23 = tk.Label(root, text="default : 0.04 (基因突变的概率)", font=('Baskerville Old Face', 10))
    label23.place(x=40, y=460)
    label24 = tk.Label(root, text="default : 0.0 (基因突变比例的衰减)", font=('Baskerville Old Face', 10))
    label24.place(x=40, y=500)

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
    text7 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text7.place(x=220, y=285)
    text8 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text8.place(x=220, y=325)
    text9 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text9.place(x=220, y=365)
    text10 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text10.place(x=220, y=405)
    text11 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text11.place(x=220, y=445)
    text12 = tk.Text(root, width=10, height=1, font=('幼圆', 10))
    text12.place(x=220, y=485)

    def get_weight1():
        weight1 = text1.get("1.0", "end-1c")  # weight-权重，用于预测的网络参数
        if weight1 == '':
            weight1 = 5
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
            weight4 = 100
        return weight4

    def get_weight5():
        weight5 = text5.get("1.0", "end-1c")
        if weight5 == '':
            weight5 = 40
        return weight5

    def get_weight6():
        weight6 = text6.get("1.0", "end-1c")
        if weight6 == '':
            weight6 = 0.1
        return weight6

    def get_weight7():
        weight7 = text7.get("1.0", "end-1c")
        if weight7 == '':
            weight7 = 0.2
        return weight7

    def get_weight8():
        weight8 = text8.get("1.0", "end-1c")
        if weight8 == '':
            weight8 = 50
        return weight8

    def get_weight9():
        weight9 = text9.get("1.0", "end-1c")
        if weight9 == '':
            weight9 = 0.03
        return weight9

    def get_weight10():
        weight10 = text10.get("1.0", "end-1c")
        if weight10 == '':
            weight10 = 0.99
        return weight10

    def get_weight11():
        weight11 = text11.get("1.0", "end-1c")
        if weight11 == '':
            weight11 = 0.04
        return weight11

    def get_weight12():
        weight12 = text12.get("1.0", "end-1c")
        if weight12 == '':
            weight12 = 0.0
        return weight12

    def next_page_jump():
        training_limit_evolution.child_screen()

    def next_page():
        p.get_input_size(get_weight1())
        p.get_hidden0(get_weight2())
        p.get_hidden1(get_weight3())
        p.get_species_size(get_weight4())
        p.get_parent_num(get_weight5())
        p.get_ansexual_rate(get_weight6())
        p.get_fitness_decay(get_weight7())
        p.get_num_gen(get_weight8())
        p.get_mutationpower(get_weight9())
        p.get_mutationpowerdecay(get_weight10())
        p.get_mutationrate(get_weight11())
        p.get_mutationratedecay(get_weight12())

        # training_limit_evolution.child_screen()

    b1 = tk.Button(root, text='使用默认参数', width=15, height=2, font=('幼圆', 12))
    b1.place(x=320, y=500)
    b2 = tk.Button(root, text='确认', command=next_page, width=15, height=2, font=('幼圆', 12))
    b2.place(x=320, y=550)
    b3 = tk.Button(root, text='开始训练', command=train, width=15, height=2, font=('幼圆', 12))
    b3.place(x=535, y=385)
    # b4 = tk.Button(root, text='查看原代码', command=check, width=15, height=2, font=('幼圆', 12))
    # b4.place(x=535, y=295)
    # b_ = tk.Button(root, text='退出', command=quit_, width=15, height=2, font=('幼圆', 12))
    # b_.place(x=660, y=550)

    label = tk.Label(root, text="请选择想查看的代码片段：", font=('幼圆', 12))
    label.place(x=440, y=10)
    b1 = tk.Button(root, text="node_update", command=leea_jpg1, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b1.place(x=440, y=40)
    b2 = tk.Button(root, text="evaluate", command=leea_jpg2, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b2.place(x=440, y=74)
    b3 = tk.Button(root, text="get_parent_index", command=leea_jpg3, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b3.place(x=440, y=108)
    b4 = tk.Button(root, text="sexual", command=leea_jpg4, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b4.place(x=440, y=142)
    b5 = tk.Button(root, text="asexual", command=leea_jpg5, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b5.place(x=440, y=176)
    b6 = tk.Button(root, text="create_first_generation", command=leea_jpg6, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b6.place(x=440, y=210)
    b7 = tk.Button(root, text="produce_offspring", command=leea_jpg7, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b7.place(x=440, y=244)
    b8 = tk.Button(root, text="get_leea_sample", command=leea_jpg8, width=22, height=1,
                   font=('Cascadia Code ExtraLight', 10))
    b8.place(x=440, y=278)
