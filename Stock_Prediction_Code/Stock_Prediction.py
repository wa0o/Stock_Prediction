import tkinter as tk  # 可视化
import random
import child_1
import child_2
import child_3
import gradient_descent
import evolution
import evolution_dynamic_sample
import limit_evolution_single
import limit_evolution
import limit_evolution_elitist
import limit_evolution_inherit
import no_training
from PIL import Image, ImageTk
import compare
import economic
from data import sample
import multiprocessing
import pyglet
import os


# path = os.getcwd() + '\\SIMYOU.TTF'
# print(path)
# pyglet.font.add_file(path)
# pyglet.font.load(path)


# 算法间性能比较图片 预测结果


# def start():  # 点击按钮后执行的函数
#     child_1.child_screen()


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


# def no_train():
#     no_training.child_screen()


def comp():
    compare.child_screen()


def quit_():
    GUI().root.quit()


class GUI:

    def __init__(self):
        self.root = tk.Tk()  # 构造窗口
        self.root.title("股票数据预测软件")  # 窗口命名
        self.root.geometry("800x350+200+100")  # 窗口大小设置

    # def button_start(self):
    #     # 添加按钮（添加按钮至窗口，按钮命名，按钮宽度，按钮高度，字体&大小）
    #     b1 = tk.Button(self.root, text='开始', command=start, width=10, height=2, font=('幼圆', 12))
    #     b1.place(x=150, y=130)  # 按钮位置设置

    # def button_quit(self):
    #     b2 = tk.Button(self.root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    #     b2.place(x=280, y=280)

    def run(self):
        font = r'C:\Users\TREE\Desktop\整合\SIMYOU.ttf'

        # 背景图片设置
        # image = Image.open("stock.JPG").resize((800, 700))
        # global image_
        # image_ = ImageTk.PhotoImage(image)
        # label_image = tk.Label(self.root, image=image_)
        # label_image.grid(row=0, column=0)

        # 显示 “已有股票模型：”
        label1 = tk.Label(self.root, text="已有股票数据：", font=('幼圆', 12))
        label1.place(x=40, y=10)

        # “股票模型”列表
        listbox = tk.Listbox(self.root, height=10, width=20, activestyle='dotbox', font=('幼圆', 12))
        # for i in range(0, 10):  # 插入股票模型（（（接口）））
        #     listbox.insert(tk.END, random.randint(100, 200))
        # listbox.place(x=40, y=30)
        listbox.insert(tk.END, '秦安股份(603758)')
        listbox.insert(tk.END, '弘讯科技(603015)')
        listbox.insert(tk.END, '合力科技(603917)')
        listbox.insert(tk.END, '洛阳玻璃(600876)')
        listbox.insert(tk.END, '金辰股份(603396)')
        listbox.insert(tk.END, '博迁新材(605376)')
        listbox.insert(tk.END, '汇得科技(603192)')
        listbox.insert(tk.END, '紫江企业(600210)')
        listbox.insert(tk.END, '福莱新材(605488)')
        listbox.insert(tk.END, '华鑫股份(600621)')
        listbox.place(x=40, y=30)

        # 将已有股票模型存入变量 stock_all
        stock_all = listbox.get(0, 9)
        # print(stock_all)

        # 显示 “请输入想预测的股票模型：”
        label2 = tk.Label(self.root, text="请输入想预测的股票数据：", font=('幼圆', 12))
        label2.place(x=40, y=210)
        label3 = tk.Label(self.root, text="(正确的股票代号，例：600000)", font=('幼圆', 12))
        label3.place(x=40, y=230)

        # 用于输入股票模型的文本框
        text = tk.Text(self.root, width=30, height=2, font=('幼圆', 12))
        text.place(x=40, y=250)

        def get_stock():  # 获取文本框中的内容
            stock = text.get("1.0", "end-1c")  # stock-股票，存放想预测的股票模型的变量（（（接口）））
            return stock

        # def next_page():
        #     stock_ = get_stock()
        #     judge = 0
        #     for j in range(0, 10):
        #         if len(stock_) >= 6:
        #             if int(stock_[0:6]) != stock_all[j]:
        #                 judge = 0
        #             else:
        #                 judge = 1
        #                 break
        #     return judge

        # def child_screen():
        #     root = tk.Toplevel()
        #     root.title("我的网络")
        #     root.geometry("400x350+200+100")
        #
        #     if next_page() == 1:
        #         image = Image.open("stock.JPG").resize((400, 350))
        #         global image_
        #         image_ = ImageTk.PhotoImage(image)
        #         label_image = tk.Label(root, image=image_)
        #         label_image.grid(row=0, column=0)
        #
        #     else:
        #         label_ = tk.Label(root, text="无已有数据！", font=('幼圆', 12))
        #         label_.place(x=150, y=130)
        #
        #     b__ = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
        #     b__.place(x=285, y=280)

        def choose_data():
            economic.create_data(get_stock())
            sample.number = get_stock()

        # ”下一页“按钮
        b = tk.Button(self.root, text='确认', command=choose_data, width=10, height=2, font=('幼圆', 12))
        b.place(x=195, y=290)

        # “退出”按钮
        b_ = tk.Button(self.root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
        b_.place(x=685, y=290)

        label = tk.Label(self.root, text="请选择训练方式：", font=('幼圆', 12))
        label.place(x=440, y=10)

        b1 = tk.Button(self.root, text='反向传播', command=gradient_des, width=15, height=2, font=('幼圆', 12))
        b1.place(x=440, y=35)
        b2 = tk.Button(self.root, text='进化', command=evo, width=15, height=2, font=('幼圆', 12))
        b2.place(x=440, y=85)
        b3 = tk.Button(self.root, text='进化(部分样本)', command=evo_dynamic_sample, width=15, height=2, font=('幼圆', 12))
        b3.place(x=440, y=135)
        b4 = tk.Button(self.root, text='有限进化', command=limit_evo_single, width=15, height=2, font=('幼圆', 12))
        b4.place(x=440, y=185)
        b5 = tk.Button(self.root, text='有限进化(多进程)', command=limit_evo, width=15, height=2, font=('幼圆', 12))
        b5.place(x=590, y=35)
        b6 = tk.Button(self.root, text='有限进化(精英)', command=limit_evo_elitist, width=15, height=2, font=('幼圆', 12))
        b6.place(x=590, y=85)
        b7 = tk.Button(self.root, text='有限进化(继承)', command=limit_evo_inherit, width=15, height=2, font=('幼圆', 12))
        b7.place(x=590, y=135)
        b8 = tk.Button(self.root, text='算法性能比较', command=comp, width=15, height=2, font=('幼圆', 12))
        b8.place(x=590, y=185)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    g = GUI()
    # g.button_start()
    # g.button_quit()
    g.run()
    g.root.mainloop()  # 使窗口保持显示状态
