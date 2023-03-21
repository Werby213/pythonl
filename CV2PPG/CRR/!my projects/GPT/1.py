import numpy as np

class Perceptron:
    def __init__(self, n_inputs, n_outputs, n_hidden_layers, n_per_hidden):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.n_hidden_layers = n_hidden_layers
        self.n_per_hidden = n_per_hidden
        self.weights = []

        # Initializing the weights randomly
        layers = [n_inputs] + [n_per_hidden]*n_hidden_layers + [n_outputs]
        for i in range(len(layers)-1):
            w = np.random.randn(layers[i], layers[i+1])
            self.weights.append(w)

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def forward(self, x):
        a = x
        for w in self.weights:
            z = np.dot(a, w)
            a = self.sigmoid(z)
        return a

# Example usage
p = Perceptron(n_inputs=2, n_outputs=1, n_hidden_layers=4, n_per_hidden=6)
x = np.random.randn(2)
output = p.forward(x)
print(output)
