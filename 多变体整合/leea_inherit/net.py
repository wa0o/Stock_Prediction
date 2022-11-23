from cgitb import small
from importlib.util import spec_from_file_location
from turtle import st
import numpy as np
from leea_inherit import function   
from data import sample
    
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

def produce_offspring(species,params):
    species.sort(key = function.getfitness,reverse=True)
    parent_num = params.parent_num/params.process_num
    parent_index = function.get_parent_index(species,int(parent_num))
    species_num = len(species)
    new_species = []
    
    for i in range (species_num):
        tmp = np.random.random()
        if tmp<params.ansexual_rate:
            child = function.asexual(species[parent_index[i][0]],params)
            new_species.append(child)
        else:
            child = function.sexual(species[parent_index[i][0]],species[parent_index[i][1]],params)
            new_species.append(child)
    
    return new_species


def evolve(species,params):
    test = sample.test_sample()
    decayrate = pow((1-params.mutationpowerdecay),1/params.num_gen)
    ratedecayrate = pow((1-params.mutationratedecay),1/params.num_gen)
    for i in range(params.num_gen):
        if i % 50 ==0 :
            print(i)
        params.mutationpower *= decayrate
        params.mutationrate *= ratedecayrate
        new_species = produce_offspring(species,params)
        test.get_leea_sample(params)
        sample_list = []
        for j in range(len(test.train_output)):
            tmp = sample.sample(test.train_input[j],test.train_output[j])
            sample_list.append(tmp)
        species = function.evaluate_all(species,sample_list,params)
        new_species = function.evaluate_all(new_species,sample_list,params)
        species = function.get_next_generation(species,new_species,len(species))
    return species