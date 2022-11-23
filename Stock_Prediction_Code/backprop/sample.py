# from doctest import OutputChecker
# import numpy as np


# class sample():
#     def __init__(self,input,output):
#         self.input =input
#         self.output = output
        
        
        
# class test_sample():
#     def __init__(self):
#         self.series_t = np.arange(0,10000,1)
#         self.series_f = 1.1+0.1*self.series_t
#         self.series_f = (self.series_f-1.1)/1000
#         self.train_input = []
#         self.train_output = []
#         self.test_input = []
#         self.test_output = []
        
    
#     def get_sample(self,params):
#         for i in range(5000):
#             index =np.random.randint(0,10000)
#             if index > 50:
#                 tmp = []
#                 for i in range(params.input_size):
#                     tmp.append(self.series_f[index-params.input_size+i])
#                 tmp.append(1)
#                 self.train_input.append(tmp)
#                 self.train_output.append(self.series_f[index])
#         for i in range(50):
#             index =np.random.randint(0,10000)
#             if index > 5:
#                 tmp = []
#                 for i in range(params.input_size):
#                     tmp.append(self.series_f[index-params.input_size+i])
#                 tmp.append(1)
#                 self.test_input.append(tmp)
#                 self.test_output.append(self.series_f[index])

from cmath import inf
import pandas as pd
import numpy as np


class sample():
    def __init__(self,input,output):
        self.input =input
        self.output = output


class test_sample():
    def __init__(self):
        data = pd.read_csv("data\zynga.csv")
        data = np.array(data)
        sample = []
        for one in data:
            sample.append(one[4])
        
        max = 0
        min = inf
        for one in sample:
            if one >max:
                max = one
            if one <min:
                min = one
        self.series_f = []
        for one in sample:
            self.series_f.append((one-min)/(max-min))
            
        self.train_input = []
        self.train_output = []
        self.test_input = []
        self.test_output = []
        
    
    def get_sample(self,params):
        for i in range(params.gen_num):
            index =np.random.randint(0,len(self.series_f))
            if index > 50:
                tmp = []
                for i in range(params.input_size):
                    tmp.append(self.series_f[index-params.input_size+i])
                tmp.append(1)                self.train_input.append(tmp)
                self.train_output.append(self.series_f[index])
        for i in range(50):
            index =np.random.randint(0,len(self.series_f))
            if index > 5:
                tmp = []
                for i in range(params.input_size):
                    tmp.append(self.series_f[index-params.input_size+i])
                tmp.append(1)
                self.test_input.append(tmp)
                self.test_output.append(self.series_f[index])

