import numpy as np
from ea import function   
    
class individual:
    def __init__(self):
        self.weight = []
        self.fitness = 0
        

    def weight_initialize (self,net_params):
        self.weight.append(net_params.weight_init*np.random.rand(net_params.hidden0,net_params.input_size+1)*2-1)
        self.weight.append(net_params.weight_init*np.random.rand(net_params.hidden1,net_params.hidden0)*2-1)
        self.weight.append(net_params.weight_init*np.random.rand(net_params.output_size,net_params.hidden1)*2-1)
        

def create_first_generation(net_params):
    
    species = []
    for i in range (net_params.species_size):
        species.append(individual())
        species[i].weight_initialize(net_params)
    return species

def produce_offspring(species,params,sample_list,parent,start): #change begin and end
    begin = int(start*params.species_size/params.process_num)
    if start == params.process_num - 1:
        end = params.species_size
    else:
        end = int((start+1)*params.species_size/params.process_num)
    new_species = []
    for i in range(begin,end):
        tmp = np.random.random()
        if tmp<params.ansexual_rate:
            child = function.asexual(species[parent[i][0]],params)
        else:
            child = function.sexual(species[parent[i][0]],species[parent[i][1]],params)
        child.fitness = function.evaluate(child,sample_list)
        new_species.append(child)
    return new_species