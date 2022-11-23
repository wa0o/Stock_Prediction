from distutils.log import error
import numpy as np
from backprop import function

class network:
    def __init__(self):
        
        self.nodeactivation = []
        self.node_size = []
        self.weight = []
        self.errors = []
    def weight_initialize (self,net_params):
        self.weight.append(net_params.weight_init*np.random.rand(net_params.hidden0,net_params.input_size+1)*10-5)
        self.weight.append(net_params.weight_init*np.random.rand(net_params.hidden1,net_params.hidden0)*10-5)
        self.weight.append(net_params.weight_init*np.random.rand(net_params.output_size,net_params.hidden1)*10-5)
        
    def node_size_initialize(self,signal_sample,net_params):
        self.node_size.append(signal_sample.input)
        for i in range(net_params.layer):
            self.node_size.append(np.zeros(len(self.weight[i])))
            for j in range (len(self.weight[i])):
                for k in range (len(self.node_size[i])):
                    self.node_size[i+1][j] = self.node_size[i][k]*self.weight[i][j][k]
    
        
    def node_update(self,signal_sample,net_params):
        self.nodeactivation = []
        self.nodeactivation.append(signal_sample.input)
        for i in range(net_params.layer):
            self.nodeactivation.append(np.zeros(len(self.weight[i])))      
            for j in range (self.weight[i].shape[0]):
                for k in range (len(self.nodeactivation[i])):
                    self.nodeactivation[i+1][j] += self.nodeactivation[i][k]*self.weight[i][j][k]
                # if i+1 != net_params.layer:
                self.nodeactivation[i+1][j] = function.sigmoid(self.nodeactivation[i+1][j])
        return self.nodeactivation[len(self.nodeactivation)-1][0]
            
    def errors_update(self,signal_sample,ans):
        self.errors = self.node_size
        self.errors[len(self.errors)-1][0] = (signal_sample.output - ans)*ans*(1-ans)
        # self.errors[len(self.errors)-1][0] = (signal_sample.output - ans)
        for i in range(len(self.errors)-1):
            j = len(self.errors)-2-i
            for k in range (len(self.errors[j])):
                error = 0
                for l in range(len(self.errors[j+1])):
                    error += self.nodeactivation[j][k]*(1-self.nodeactivation[j][k])*self.errors[j+1][l]*self.weight[j][l][k]
                self.errors[j][k] = error

    def weight_update(self,learning_rate):
        for j in range(len(self.weight)):
            for k in range(len(self.weight[j])):
                for l in range(len(self.weight[j][k])):
                    self.weight[j][k][l] += self.nodeactivation[j][l]*self.errors[j+1][k]*learning_rate
