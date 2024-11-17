# main.py
import numpy as np
from perceptron import Perceptron

def load_data(filepath):
    # Load data from the text file
    data = np.loadtxt(filepath, delimiter=',')
    X = data[:, :2]  # Features x1 and x2, X contains the features (x1 and x2).
    y = data[:, 2]   # Labels, y contains the labels (either 1 or -1 for binary classification)
    return X, y

def main():
    # Load data
    X, y = load_data('data/data.txt')

    # Initialize and train Perceptron
    # Initializes a Perceptron object with a learning rate of 0.1 and a maximum of 1000 epochs (iterations).
    perceptron = Perceptron(learning_rate=0.1, max_epochs=1000)
    perceptron.train(X, y) # Trains the Perceptron using the training data (X and y).

    # Test prediction (optional, can add test samples here)
    sample = np.array([0.3, 0.8])
    prediction = perceptron.predict(sample)
    print(f"Prediction for sample {sample}: {prediction}")

if __name__ == "__main__":
    main()
