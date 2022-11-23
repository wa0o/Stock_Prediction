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
        self.mutationratedecay = 0
        self.test_num = 50
        self.batch_num = 3