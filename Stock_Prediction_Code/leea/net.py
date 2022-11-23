from importlib.util import spec_from_file_location
import numpy as np
from leea import function


class individual:
    def __init__(self):
        self.weight = []
        self.fitness = 0

    def weight_initialize(self, net_params):
        self.weight.append(
            net_params.weight_init * np.random.rand(net_params.hidden0, net_params.input_size + 1) * 2 - 1)
        self.weight.append(net_params.weight_init * np.random.rand(net_params.hidden1, net_params.hidden0) * 2 - 1)
        self.weight.append(net_params.weight_init * np.random.rand(net_params.output_size, net_params.hidden1) * 2 - 1)


def create_first_generation(net_params):
    species = []
    for i in range(net_params.species_size):
        species.append(individual())
        species[i].weight_initialize(net_params)
    return species


def produce_offspring(species, parent_num, params):
    species.sort(key=function.getfitness, reverse=True)
    parent_index = function.get_parent_index(species, parent_num)
    species_num = len(species)
    new_species = []

    for i in range(species_num):
        tmp = np.random.random()
        if tmp < params.ansexual_rate:
            child = function.asexual(species[parent_index[i][0]], params)
            new_species.append(child)
        else:
            child = function.sexual(species[parent_index[i][0]], species[parent_index[i][1]], params)
            new_species.append(child)

    return new_species
