import tkinter as tk
import random
import child_2
import child_3


def quit_():
    tk.Tk().quit()


def child_screen():
    root = tk.Tk()
    root.title("我的网络")
    root.geometry("400x350+200+100")

    # 显示 “已有股票模型：”
    label1 = tk.Label(root, text="已有股票模型：", font=('幼圆', 12))
    label1.place(x=40, y=10)

    # “股票模型”列表
    listbox = tk.Listbox(root, height=10, width=20, activestyle='dotbox', font=('幼圆', 12))
    for i in range(0, 10):  # 插入股票模型（（（接口）））
        listbox.insert(tk.END, random.randint(100, 200))
    listbox.place(x=40, y=30)

    # 将已有股票模型存入变量 stock_all
    stock_all = listbox.get(0, 9)
    # print(stock_all)

    # 显示 “请输入想预测的股票模型：”
    label2 = tk.Label(root, text="请输入想预测的股票模型：", font=('幼圆', 12))
    label2.place(x=40, y=210)

    # 用于输入股票模型的文本框
    text = tk.Text(root, width=30, height=2, font=('幼圆', 12))
    text.place(x=40, y=230)

    def get_stock():  # 获取文本框中的内容
        stock = text.get("1.0", "end-1c")  # stock-股票，存放想预测的股票模型的变量（（（接口）））
        return stock

    def next_page():
        stock_ = get_stock()
        judge = False
        for j in range(0, 10):
            if len(stock_) >= 3:
                if int(stock_[0:3]) != stock_all[j]:
                    judge = False
                else:
                    judge = True
                    break
        if judge:
            child_2.child_screen()
        else:
            child_3.child_screen()

    # ”下一页“按钮
    b = tk.Button(root, text='下一页', command=next_page, width=10, height=2, font=('幼圆', 12))
    b.place(x=195, y=280)

    # “退出”按钮
    b_ = tk.Button(root, text='退出', command=quit_, width=10, height=2, font=('幼圆', 12))
    b_.place(x=285, y=280)
