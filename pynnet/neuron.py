import numpy


class Neuron(object):
    """
    Class representing a single neuron, which accepts an array as input and
    produces a single value as output.
    """
    def __init__(self, size):
        """
        Initialize the neuron with random weights.

        @param size - size of the input neuron can accept
        """
        self._weights = numpy.random.random(size)

    def _sigmoid(self, values):
        """
        Helper function - calculates the output of the neuron

        @param values - input to run through the neuron
        """
        return 1.0 / (1 + numpy.exp(-numpy.dot(self._weights, values)))
        
    def synapse(self, values):
        """
        Calculates the output value of this neuron, given the current weight values

        @param values - input to run through the neuron
        @return a double in the range of 0-1.0
        """
        if len(values) != len(self._weights):
            raise ValueError("Input must be equal in length to neurons weights.")

        return self._sigmoid(values)
