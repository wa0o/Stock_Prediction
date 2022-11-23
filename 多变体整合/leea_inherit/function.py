from distutils.spawn import find_executable
from lib2to3.pgen2.literals import simple_escapes
import re
import numpy as np
from leea_inherit import net

def sigmoid(x):
    # if x<0:
    #     return 0
    # else:
    #     return x
    #return abs(x)
    return 1/(1+np.exp(-4.9*x))


def learing_rate_decay(learing_rate,learing_decay):
    learing_rate *= (1-learing_decay)
    return learing_rate

def node_update(signal_sample,one):
    nodeactivation = []
    nodeactivation.append(signal_sample.input)
    for i in range(len(one.weight)):
        nodeactivation.append(np.zeros(len(one.weight[i])))
        for j in range (one.weight[i].shape[0]):
            for k in range (len(nodeactivation[i])):
                nodeactivation[i+1][j] += nodeactivation[i][k]*one.weight[i][j][k]
            # if i+1 != len(one.weight):
            nodeactivation[i+1][j] = sigmoid(nodeactivation[i+1][j])
    return nodeactivation[len(nodeactivation)-1][0]

def evaluate(individual,sample_list):
    fitness = len(sample_list)
    for sample in sample_list:
        ans = node_update(sample,individual)
        fitness -= (ans-sample.output)*(ans-sample.output)
    return fitness

def evaluate_all(species,sample_list,params):
    for i in range(len(species)):
        species[i].fitness *= (1-params.fitness_decay)
        fit = evaluate(species[i],sample_list)
        species[i].fitness +=fit
    return species

def getfitness(individual):
    return individual.fitness


def get_parent_index(species,parent_num):
    parent = []
    probabilities = np.zeros(parent_num)
    probability = 0
    for i in range (parent_num):
        parent.append(species[i])
        probabilities[i] = parent[i].fitness
        probability+=parent[i].fitness
    for i in range(len(probabilities)):
        probabilities[i] = probabilities[i]/probability
        
    index_list = np.arange(0,parent_num,1)
    parent_list = []
    for i in range(len(species)):
        index1 = np.random.choice(index_list, p = probabilities.ravel())
        index2 = np.random.choice(index_list, p = probabilities.ravel())
        parent_list.append((index1,index2))
    return parent_list    
    

def sexual(parent1,parent2,params):
    proportion = parent1.fitness/(parent1.fitness+parent2.fitness)
    child  = net.individual()
    child.weight_initialize(params)
    for i in range(len(child.weight)):
        for j in range(len(child.weight[i])):
            for k in range(len(child.weight[i][j])):
                child.weight[i][j][k] = parent1.weight[i][j][k]
                if(np.random.random()>proportion):
                    child.weight[i][j][k] = parent2.weight[i][j][k]
    child.fitness = parent1.fitness*proportion + parent2.fitness*(1-proportion)
    return child

def asexual(parent1,params):
    child  = net.individual()
    child.weight_initialize(params)
    for i in range(len(child.weight)):
        for j in range(len(child.weight[i])):
            for k in range(len(child.weight[i][j])):
                child.weight[i][j][k] = parent1.weight[i][j][k]
                if(np.random.random()<params.mutationrate):
                    child.weight[i][j][k] += np.random.rand()*params.mutationpower*2-params.mutationpower
    child.fitness = parent1.fitness
    return child

def divide(species,params,start):
    begin = start*params.species_size/params.process_num
    if start == params.process_num - 1:
        end = params.species_size
    else:
        end = (start+1)*(params.species_size/params.process_num)
    small_species = []
    for i in range(int(begin),int(end)):
        small_species.append(species[i])
    return small_species

def get_next_generation(species1,species2,species_size): #change here
    tmp = species1
    tmp.extend(species2)
    tmp.sort(key = getfitness,reverse=True)
    tmp2 = []
    for i in range(species_size):
        tmp2.append(tmp[i])
    return tmp2