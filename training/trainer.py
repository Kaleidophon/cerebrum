from neural.neuron import Neuron
from neural.cerebrum import Cerebrum, Input

import numpy


def sigmoid(z):
    return 1.0 / (1.0 + numpy.exp(-1.0 * z))


class Trainer(object):

    def __init__(self):
        self.build_line()

    def build_line(self):
        neuron1 = Neuron(3, sigmoid)
        neuron2 = Neuron(4, sigmoid)
        neuron3 = Neuron(5, sigmoid, output=True)
        input1 = Input(0, 3)
        input2 = Input(1, 2.4)
        input3 = Input(2, -3.4)

        connections = {0: 3, 1: 3, 2: 3, 3: 4, 4: 5}
        neurons = [input1, input2, input3, neuron1, neuron2, neuron3]

        cere = Cerebrum(neurons, connections)
        cere.start()


if __name__ == "__main__":
    trainer = Trainer()
