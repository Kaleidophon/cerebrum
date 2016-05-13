from neural.neuron import Neuron
from neural.cerebrum import Cerebrum, Input
import numpy as np


import numpy
from util.drawer import draw_network


def sigmoid(z):
    return 1.0 / (1.0 + numpy.exp(-1.0 * z))


def elu(z, alpha=1.0):
    if z >= 0:
        return z
    else:
        return alpha * (np.exp(z) - 1)


class Trainer(object):

    def __init__(self):
        self.build_line()

    def build_line(self):
        neuron1 = Neuron(3, sigmoid)
        neuron2 = Neuron(4, sigmoid)
        neuron3 = Neuron(5, sigmoid)
        neuron4 = Neuron(6, sigmoid)
        neuron5 = Neuron(7, sigmoid)
        neuron6 = Neuron(8, sigmoid, output=True)

        input1 = Input(0, 3)
        input2 = Input(1, 2.4)
        input3 = Input(2, -3.4)

        connections = {3: [0, 1, 2], 4: [0, 1, 2], 5: [0, 1, 2], 6: [3, 4, 5],
                       7: [3, 4, 5], 8: [7]}
        neurons = [input1, input2, input3, neuron1, neuron2, neuron3,
                   neuron4, neuron5, neuron6]

        cere = Cerebrum(neurons, connections)
        cere.start()

        draw_network(neurons, connections)


if __name__ == "__main__":
    trainer = Trainer()
