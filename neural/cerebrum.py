

class Cerebrum(object):

    def __init__(self, neurons, connections):
        self.outputs = [neuron for neuron in neurons if neuron.is_output()]

        print "Connections:"
        for (neur, incoming) in connections.items():
            print "{%s} -> %i" % (", ".join([str(n) for n in incoming]), neur)
            for inc in incoming:
                neurons[neur].add_incoming(neurons[inc])

        for neuron in neurons:
            neuron.init_weights()

    def start(self):
        print "\nStart brain!"
        for output_neuron in self.outputs:
            print output_neuron.compute_activation()
