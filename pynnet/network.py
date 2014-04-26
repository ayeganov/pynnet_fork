import layer


class NeuralNetwork(object):
    """
    Class representing a neural network.
    """
    def __init__(self, input_size, layer_sizes):
        """
        Initialize a neural network to accept a signal of a specified size, and
        containing a number of layers equal to the length of the layer_sizes
        array.

        @param input_size - length of the signal this network can process
        @param layer_sizes - an array of layer sizes, length of this array
                             represents the number of layers in the network
        """
        if input_size <= 0 or 0 in layer_sizes:
            raise ValueError("All layers must accept and return positive signals.")
        self._layers = []
        for layer_size in layer_sizes:
            self._layers.append(layer.Layer(in_size, input_size)
            input_size = layer_size

    def feed_forward(self, input_signal):
        pass

    def __repr__(self):
        return {'layers':self._layers}
