
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def learing_rate_decay(learing_rate,learing_decay):
    learing_rate *= (1-learing_decay)
    return learing_rate