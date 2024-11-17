# perceptron.py
import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, max_epochs=1000): #
        self.learning_rate = learning_rate #learning_rate: The step size for updating the weights.
        self.max_epochs = max_epochs #max_epochs: The maximum number of training iterations.
        self.w = None #w: The weights (initialized later).
        self.b = None #b: The bias (initialized later).

    def initialize_parameters(self, num_features):
        # Initialize weights and bias randomly
        # Initializes the weights (w) and bias (b) randomly using NumPy's random.rand().
        self.w = np.random.rand(num_features)
        self.b = np.random.rand()

    def predict(self, X):
        # Calculate output: 1 if w * x + b > 0 else -1
        # Uses the dot product of the input features and weights (w * x + b).
        linear_output = np.dot(X, self.w) + self.b
        return np.where(linear_output > 0, 1, -1)

    def train(self, X, y):
        # Initialize weights and bias
        self.initialize_parameters(X.shape[1])

        for epoch in range(self.max_epochs):
            errors = 0
            for i in range(len(y)):
                x_i = X[i]
                y_pred = self.predict(x_i)

                # Calculate error
                error = y[i] - y_pred

                # Update weights and bias if there is an error
                if error != 0:
                    self.w += self.learning_rate * error * x_i
                    self.b += self.learning_rate * error
                    errors += 1

            # Stop training if no errors (convergence)
            if errors == 0:
                print(f"Converged after {epoch + 1} epochs.")
                break

        print(f"Final weights: {self.w}")
        print(f"Final bias: {self.b}")
