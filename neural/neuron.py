import numpy


class Neuron(object):

    def __init__(self, id, activation_function, omega=0.3, output=False):
        self.id = id
        self.activation_function = activation_function
        self.incoming = []
        self.weights = []
        self.omega = omega
        self.output = output
        self.neural_pool = None

    def compute_activation(self):
        input = numpy.array([neuron.compute_activation() for neuron in self.incoming])
        print "Input Neuron #%i: %s" %(self.id, str(input))
        return self.activation_function(numpy.dot(input, self.weights)) + 1

    def pick_new_incoming(self):
        self.incoming.append(self.neuron_pool.pop())
        # TODO: How to initialize a new weight
        self.weights = numpy.append(self.weights, 1)

    def set_neural_pool(self, neural_pool):
        self.neural_pool = neural_pool

    def add_incoming(self, neuron):
        self.incoming.append(neuron)

    def remove_incoming(self, i):
        self.incoming.pop(i)
        self.weights.pop(i)

    def init_weights(self):
        self.weights = numpy.random.uniform(size=len(self.incoming))

    def is_output(self):
        return self.output

    def get_id(self):
        return self.id

