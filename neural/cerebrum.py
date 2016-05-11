

class Cerebrum(object):

    def __init__(self, neurons, connections):
        self.outputs = [neuron for neuron in neurons if neuron.is_output()]

        print "Connections:"
        for (start, end) in connections.items():
            print "%i - %i" %(start, end)
            neurons[end].add_incoming(neurons[start])

        for neuron in neurons:
            neuron.init_weights()

    def start(self):
        print "\nStart brain!"
        for output_neuron in self.outputs:
            print output_neuron.compute_activation()


class Input(object):

    def __init__(self, id, x_i):
        self.id = id
        self.x_i = x_i
        self.incoming = None

    def compute_activation(self):
        return self.x_i

    def is_output(self):
        return False

    def init_weights(self):
        pass
