class net_params:
    def __init__(self):
        self.layer = 3
        self.input_size = 4
        self.hidden0 = 50
        self.hidden1 = 20
        self.output_size = 1
        self.weight_init = 1
        self.learing_rate = 0.1
        self.learing_decat = 0.1
        self.gen_num = 10000
        self.test_num = 50

    def get_input_size(self, input_size):
        self.input_size = int(input_size)

    def get_hidden0(self, hidden0):
        self.hidden0 = int(hidden0)

    def get_hidden1(self, hidden1):
        self.hidden1 = int(hidden1)

    def get_learing_rate(self, learing_rate):
        self.learing_rate = float(learing_rate)

    def get_learing_decat(self, learing_decat):
        self.learing_decat = float(learing_decat)

    def get_gen_num(self, gen_num):
        self.gen_num = int(gen_num)
