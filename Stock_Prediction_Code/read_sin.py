from operator import length_hint
import pickle
import numpy as np
import matplotlib.pyplot as plt

# backprop.backprop_experiment().............1
# ea.ea_experiment().........................3
# leea.leea_experiment().....................4
# leea_elitist.leea_experiment().............5
# leea_inherit.leea_experiment().............6
# ea_dynamic_sample.leea_experiment()........7

def show_one(num):
    size = 1
    batch_num = 1
    length = 1
    if num == 1:
        length = 100
        f = open('summary_sin\\back.pkl','rb')
        y1,y2 = pickle.load(f)
        for i in range(len(y1)):
            for j in range(len(y1[0])):
                y1[i][j] = abs(y1[i][j])
    if num == 3:
        f = open('summary_sin\\e_a.pkl','rb')
        y1,y2,size,batch_num = pickle.load(f)
    if num == 4:
        f = open('summary_sin\\le_ea.pkl','rb')
        y1,y2,size,batch_num = pickle.load(f)
    if num == 5:
        f = open('summary_sin\\elitist.pkl','rb')
        y1,y2,size,batch_num = pickle.load(f)
    if num == 6:
        f = open('summary_sin\\inherit.pkl','rb')
        y1,y2,size,batch_num = pickle.load(f)
    if num == 7:
        f = open('summary_sin\\dynamic.pkl','rb')
        y1,y2,size,batch_num,length = pickle.load(f)
    if num != 7:
        x = np.arange(0.0,len(y1[0]),1.0)*size*batch_num*length
    if num == 7:
        x = np.zeros(len(y2[0]))
        for i in range(len(x)):
            if i % 50 == 0 and i != 0:
                x[i] += x[i - 1] + size * length
            elif i == 0:
                x[i] = size * batch_num
            else:
                x[i] += x[i - 1] + size * batch_num
    sum = np.zeros((2,len(y1[0])))
    y = np.zeros((len(y1),len(y1[0])))
    for j in range(len(y1[0])):
        for i in range(len(y1)):
            y[i][j] = y1[i][j]
            sum[0][j] += y[i][j]
            sum[1][j] += y2[i][j]
        sum[0][j] /= len(y1)
        sum[1][j] /= len(y1)

    for i in range(len(y1)):
        plt.subplot2grid((4,4),(int(i/4),i%4))
        plt.plot(x,y[i],x,y2[i])
        plt.xlabel('number_of_used_data')
        plt.ylabel('error')
        plt.legend(['train', 'test'])
    plt.show()
    plt.plot(x,sum[0],x,sum[1])
    plt.xlabel('number_of_used_data')
    plt.ylabel('error')
    plt.legend(['train', 'test'])
    plt.title('15 times average result')
    plt.show()

def csum(y1,y2):
    sum = np.zeros((2,len(y1[0])))
    y = np.zeros((len(y1),len(y1[0])))
    for j in range(len(y1[0])):
        for i in range(len(y1)):
            y[i][j] = y1[i][j]
            sum[0][j] += y[i][j]
            sum[1][j] += y2[i][j]
        sum[0][j] /= len(y1)
        sum[1][j] /= len(y1)
    return sum[1]

def showpart1():
    size = 1
    batch_num = 1
    f = open('summary_sin\\back.pkl','rb')
    y,y1 = pickle.load(f)
    x = np.arange(0.0,len(y1[0]),1.0)*100
    plt.plot(x,csum(y,y1))

    f = open('summary_sin\\e_a.pkl','rb')
    y,y2,size,batch_num = pickle.load(f)
    x = np.arange(0.0,len(y2[0]),1.0)*size*batch_num
    plt.plot(x,csum(y,y2))

    f = open('summary_sin\\le_ea.pkl','rb')
    y,y3,size,batch_num = pickle.load(f)
    x = np.arange(0.0,len(y3[0]),1.0)*size*batch_num
    plt.plot(x,csum(y,y3))

    plt.legend(['backprop','ea','leea'])
    plt.xlabel('number_of_used_data')
    plt.ylabel('error')
    plt.show()


def showpart2():
    f = open('summary_sin\\le_ea.pkl','rb')
    y,y1,size,batch_num = pickle.load(f)
    x = np.arange(0.0,len(y1[0]),1.0)*size*batch_num
    plt.plot(x[0:int(len(x)/4)],csum(y,y1)[0:int(len(x)/4)])
    

    f = open('summary_sin\\elitist.pkl','rb')
    y,y2,size,batch_num = pickle.load(f)
    x = np.arange(0.0,len(y2[0]),1.0)*size*batch_num
    plt.plot(x[0:int(len(x)/4)],csum(y,y2)[0:int(len(x)/4)])

    f = open('summary_sin\\inherit.pkl','rb')
    y,y3,size,batch_num = pickle.load(f)
    x = np.arange(0.0,len(y3[0]),1.0)*size*batch_num
    plt.plot(x[0:int(len(x)/4)],csum(y,y3)[0:int(len(x)/4)])
    f = open('summary_sin\\dynamic.pkl', 'rb')
    y, y4, size, batch_num, length = pickle.load(f)
    x = np.zeros(len(y4[0]))
    for i in range(len(x)):
        if i % 50 == 0 and i != 0:
            x[i] += x[i-1] + size * length
        elif i == 0:
            x[i] = size*batch_num
        else:
            x[i] += x[i-1] + size * batch_num
    plt.plot(x[0:int(len(y4[0])/8)], csum(y, y4)[0:int(len(y4[0])/8)])
    plt.legend(['leea','leea_elitist','leea_inherit', 'leea_dynamic_sample'])
    plt.xlabel('number_of_used_data')
    plt.ylabel('error')
    plt.show()


# show_one(1)
# showpart1()
# showpart2()

