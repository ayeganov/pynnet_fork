import neuron

class Layer(object):
    """
    Class representing a single layer in the neural network
    """
    def __init__(self, num_neurons, input_size):
        """
        Initialzes the layer with the specified number of neurons, each of the
        given size.

        @param num_neurons - number of neurons in this layer
        @param input_size - length of signal each neuron must be able to process
        """
        self._neurons = [neuron.Neuron(input_size) for _ in range(num_neurons)]

    def processSignal(self, signal):
        """
        Takes in an array representing a signal to
        be learned, or recognized by the neural network

        @param signal - signal to learn, orrecognize
        """
        return [neuron.synapse(signal) for neuron in self._neurons]
