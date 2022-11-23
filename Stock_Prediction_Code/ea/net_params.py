class net_params:
    def __init__(self):
        self.layer = 3
        self.input_size = 5
        self.hidden0 = 50
        self.hidden1 = 20
        self.output_size = 1
        self.weight_init = 1
        self.species_size = 100
        self.parent_num = 40
        self.ansexual_rate = 0.1
        self.fitness_decay = 0.2
        self.num_gen = 50
        self.mutationpower = 0.03
        self.mutationpowerdecay = 0.99
        self.mutationrate = 0.04
        self.mutationratedecay = 0.0
        self.process_num = 8
        self.test_num = 50

    def get_input_size(self, input_size):
        self.input_size = int(input_size)

    def get_hidden0(self, hidden0):
        self.hidden0 = int(hidden0)

    def get_hidden1(self, hidden1):
        self.hidden1 = int(hidden1)

    def get_species_size(self, species_size):
        self.species_size = int(species_size)

    def get_parent_num(self, parent_num):
        self.parent_num = int(parent_num)

    def get_ansexual_rate(self, ansexual_rate):
        self.ansexual_rate = float(ansexual_rate)

    def get_fitness_decay(self, fitness_decay):
        self.fitness_decay = float(fitness_decay)

    def get_num_gen(self, num_gen):
        self.num_gen = int(num_gen)

    def get_mutationpower(self, mutationpower):
        self.mutationpower = float(mutationpower)

    def get_mutationpowerdecay(self, mutationpowerdecay):
        self.mutationpowerdecay = float(mutationpowerdecay)

    def get_mutationrate(self, mutationrate):
        self.mutationrate = float(mutationrate)

    def get_mutationratedecay(self, mutationratedecay):
        self.mutationratedecay = float(mutationratedecay)

    def get_process_num(self, process_num):
        self.process_num = int(process_num)
