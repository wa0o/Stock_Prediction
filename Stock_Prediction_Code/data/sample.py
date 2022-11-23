from cmath import inf
import pandas as pd
import numpy as np


number = 603758  # 默认训练的股票数据集


class sample:
    def __init__(self, input, output):
        self.input = input
        self.output = output


class test_sample:
    def __init__(self):
        data = pd.read_csv("data\\"+str(number)+".csv")
        print("训练的股票数据集代号为：", number)
        data = np.array(data)
        sample = []
        for one in data:
            sample.append(one[6])
        
        max = 0
        min = inf
        for one in sample:
            if one > max:
                max = one
            if one < min:
                min = one
        self.series_f = []
        for one in sample:
            self.series_f.append((one-min)/(max-min))
            
        self.train_input = []
        self.train_output = []
        self.test_input = []
        self.test_output = []
        
    def get_back_sample(self, params):
        for i in range(params.gen_num):
            index = np.random.randint(0, len(self.series_f)/2)
            if index > params.input_size:
                index = index*2
                tmp = []
                for i in range(params.input_size):
                    tmp.append(self.series_f[index-params.input_size+i])
                tmp.append(1)
                self.train_input.append(tmp)
                self.train_output.append(self.series_f[index])
    
    def get_ea_sample(self, params):  # change here
        for i in range(params.input_size, int(len(self.series_f)/2)-1):
            index = i * 2
            tmp = []
            for i in range(params.input_size):
                tmp.append(self.series_f[index-params.input_size+i])
            tmp.append(1)
            self.train_input.append(tmp)
            self.train_output.append(self.series_f[index])
                
    def get_leea_sample(self, params):  # change here
        self.train_input = []
        self.train_output = []
        i = 0
        while i < params.batch_num:
            index = np.random.randint(0, len(self.series_f))
            if index > params.input_size and index % 2 == 0:
                i += 1
                tmp = []
                for j in range(params.input_size):
                    tmp.append(self.series_f[index-params.input_size+j])
                tmp.append(1)
                self.train_input.append(tmp)
                self.train_output.append(self.series_f[index])
    
    def get_test_sample(self, params):
        for i in range(int(len(self.series_f))):
            if i % 4 == 1 and i > params.input_size:
                tmp = []
                index = i
                for j in range(params.input_size):
                    tmp.append(self.series_f[index-params.input_size+j])
                tmp.append(1)
                self.test_input.append(tmp)
                self.test_output.append(self.series_f[index])
        
