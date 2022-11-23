def backprop_experiment():
    from data import sample
    from backprop import net_params
    from backprop import net
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    import gradient_descent
    import tkinter as tk

    matplotlib.rc("font", family='YouYuan')

    par = gradient_descent.p
    print(par.input_size)
    print(par.hidden0)
    print(par.hidden1)
    print(par.learing_rate)
    print(par.learing_decat)
    print(par.gen_num)

    sam = sample.test_sample()
    sam.get_back_sample(par)
    sam.get_test_sample(par)

    network = net.network()

    signalsample = sample.sample(sam.train_input[0],sam.train_output[0])
    network.weight_initialize(par)
    network.node_size_initialize(signalsample,par)

    x1 = np.arange(0.0, len(sam.train_output), 1.0)
    y = np.arange(0.0, len(sam.train_output), 1.0)

    for i in range(len(sam.train_output)):
        signalsample = sample.sample(sam.train_input[i],sam.train_output[i])
        ans = network.node_update(signalsample,par)
        err=network.errors_update(signalsample,ans)
        network.weight_update(par.learing_rate)
        y[i] = abs(ans-signalsample.output)
        if i % 100 ==0:
            if i%500==0:
                par.learing_rate *=(1-par.learing_decat)
            print(i)
            plt.plot(i,abs(ans-signalsample.output),marker = '.',color = 'black')
            plt.ylabel('error')
            plt.draw()
            plt.pause(0.01)
    plt.pause(2)
    plt.close()

    # plt.plot(x1, y)
    # plt.title('backprop-|predict-fact|')
    # plt.xlabel('generation')
    # plt.ylabel('|predict-fact|')
    # plt.show()

    x2 = np.arange(0.0, len(sam.test_output), 1.0)
    z1 = np.arange(0.0, len(sam.test_output), 1.0)
    z2 = np.arange(0.0, len(sam.test_output), 1.0)

    for i in range(len(sam.test_output)):
        signalsample = sample.sample(sam.test_input[i],sam.test_output[i])
        ans = network.node_update(signalsample,par)
        z1[i] = ans
        z2[i] = signalsample.output
        # print(ans,signalsample.output)

    plt.title('backprop')
    plt.plot(x2, z1, x2, z2)
    plt.legend(['predict', 'true'])
    plt.xlabel('time')
    plt.ylabel('The Normalized Stock Price')
    plt.show()

    # root = tk.Tk()
    # root.title("预测结果")
    # root.geometry("400x300+200+20")
    #
    # label = tk.Label(root, text="预测结果 预测结果", font=('幼圆', 12))
    # label.place(x=120, y=120)
