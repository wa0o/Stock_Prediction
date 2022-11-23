from concurrent.futures import process
import numpy as np
from ea import net
from threading import Thread
from multiprocessing import Pool
from multiprocessing import Process


def sigmoid(x):
    return 1 / (1 + np.exp(-4.9 * x))


def learing_rate_decay(learing_rate, learing_decay):
    learing_rate *= (1 - learing_decay)
    return learing_rate


def node_update(signal_sample, one):
    nodeactivation = []
    nodeactivation.append(signal_sample.input)
    for i in range(len(one.weight)):
        nodeactivation.append(np.zeros(len(one.weight[i])))
        for j in range(one.weight[i].shape[0]):
            for k in range(len(nodeactivation[i])):
                nodeactivation[i + 1][j] += nodeactivation[i][k] * one.weight[i][j][k]
            nodeactivation[i + 1][j] = sigmoid(nodeactivation[i + 1][j])
    return nodeactivation[len(nodeactivation) - 1][0]


def evaluate(individual, sample_list):
    fitness = len(sample_list)
    for sample in sample_list:
        ans = node_update(sample, individual)
        fitness -= (ans - sample.output) * (ans - sample.output)
    return fitness


def evaluate_all(species, sample_list):
    for i in species:
        i.fitness = evaluate(i, sample_list)
    return species


def pro_evaluate_all(species,sample_list,params):#change here
    tmp = []
    pool = Pool(processes=params.process_num)
    for individual in species:
        one = pool.apply_async(evaluate,args=(individual,sample_list,))
        tmp.append(one)
    pool.close()
    pool.join
    for i in range(len(tmp)):
        species[i].fitness = (tmp[i].get())


def th_evaluate_all(species, sample_list, start, params):
    start = start * params.species_size / params.process_num
    for i in range(int(start), int(start + params.species_size / params.thread_num)):
        species[i].fitness = evaluate(species[i], sample_list)


def getfitness(individual):
    return individual.fitness


def get_parent_index(species, parent_num):
    parent = []
    probabilities = np.zeros(parent_num)
    probability = 0
    for i in range(parent_num):
        parent.append(species[i])
        probabilities[i] = parent[i].fitness
        probability += parent[i].fitness
    for i in range(len(probabilities)):
        probabilities[i] = probabilities[i] / probability

    index_list = np.arange(0, parent_num, 1)
    parent_list = []
    for i in range(len(species)):
        index1 = np.random.choice(index_list, p=probabilities.ravel())
        index2 = np.random.choice(index_list, p=probabilities.ravel())
        parent_list.append((index1, index2))
    return parent_list


def sexual(parent1, parent2, net_params):
    child = net.individual()
    child.weight_initialize(net_params)
    for i in range(len(child.weight)):
        for j in range(len(child.weight[i])):
            for k in range(len(child.weight[i][j])):
                child.weight[i][j][k] = parent1.weight[i][j][k]
                if np.random.random() > 0.5:
                    child.weight[i][j][k] = parent2.weight[i][j][k]
    child.fitness = 0
    return child


def asexual(parent1, net_params):
    child = net.individual()
    child.weight_initialize(net_params)
    for i in range(len(child.weight)):
        for j in range(len(child.weight[i])):
            for k in range(len(child.weight[i][j])):
                child.weight[i][j][k] = parent1.weight[i][j][k]
                if np.random.random() < net_params.mutationrate:
                    child.weight[i][j][k] += np.random.rand() * net_params.mutationpower * 2 - \
                                             net_params.mutationpower
    child.fitness = 0
    return child


def get_next_generation(species1, species2, species_size):
    tmp = species1
    for individual in species2:
        tmp.append(individual)
    tmp.sort(key=getfitness, reverse=True)
    tmp2 = []
    for i in range(species_size):
        tmp2.append(tmp[i])
    return tmp2


def work(species, params, sample_list):
    thread_list = []
    new_species = [None] * params.species_size
    start = 0
    for i in range(params.thread_num):
        thread_list.append(Thread(target=net.produce_offspring, args=(species, params, new_species, start)))
        start = start + params.species_size / params.thread_num

    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

    thread_list = []
    start = 0
    for i in range(params.thread_num):
        thread_list.append(Thread(target=th_evaluate_all, args=(new_species, sample_list, start, params)))
        start = start + params.species_size / params.thread_num

    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    return new_species
