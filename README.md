# Perceptron Algorithm

A simple implementation of the Perceptron learning algorithm for binary classification in Python.

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [How the Perceptron Works](#how-the-perceptron-works)
- [Dataset Format (`data.txt`)](#dataset-format-datatxt)
- [Prediction](#prediction)
- [Training the Perceptron](#training-the-perceptron)
- [Example Iteration](#example-iteration)
- [How to Run the Project](#how-to-run-the-project)
- [Example Output](#example-output)
- [Customization](#customization)
- [References](#references)
- [License](#license)

## Introduction

The **Perceptron** is a simple and effective machine learning model used for binary classification tasks. It learns to separate data points into two classes based on their input features. This project demonstrates the Perceptron algorithm using Python, showcasing how it can learn a decision boundary for classification problems.

## Project Overview

The goal of this project is to:

1. Implement the Perceptron learning algorithm.
2. Use a dataset (`data.txt`) for training the Perceptron model.
3. Classify new data points based on the learned decision boundary.

### Key Components
- **Weights** (`w1`, `w2`): Determines the influence of input features on the output.
- **Bias** (`b`): Shifts the decision boundary.
- **Learning Rate**: Controls the speed of learning and weight updates.

## How the Perceptron Works

The Perceptron algorithm iteratively adjusts weights and bias to find a linear decision boundary that separates the data points of two classes.

1. **Initialization**: Randomly initialize the weights and bias.
2. **Prediction**: Compute the weighted sum of the inputs.
3. **Update**: If the prediction is incorrect, adjust the weights and bias based on the error.

### Formula:
output = (w1 * x1) + (w2 * x2) + b

javascript
Copy code

- If `output > 0`, the predicted class is `1`.
- If `output <= 0`, the predicted class is `-1`.

## Dataset Format (`data.txt`)

The training data is stored in `data.txt`, which contains the input features and labels.

### Example of `data.txt`:
0.2, 0.4, 1 0.4, 0.6, 1 0.6, 0.8, 1 0.8, 0.4, -1 0.3, 0.7, -1

markdown
Copy code

- The first two values are the input features (`x1`, `x2`).
- The third value is the label (`y`), where:
    - `1` represents Class 1 (e.g., positive class).
    - `-1` represents Class -1 (e.g., negative class).

## Prediction

**Prediction** refers to classifying a new data point after the Perceptron has been trained. Given a new input (e.g., `[0.5, 0.5]`), the model uses the learned weights and bias to compute the output:

output = (w1 * 0.5) + (w2 * 0.5) + b

markdown
Copy code

- If the output is positive, the model predicts Class `1`.
- If the output is negative, the model predicts Class `-1`.

## Training the Perceptron

The training process involves the following steps:

1. Initialize weights (`w1`, `w2`) and bias (`b`).
2. For each data point in `data.txt`:
    - Compute the predicted output using the formula.
    - Compare the predicted output with the actual label.
    - If the prediction is incorrect, update the weights and bias.

### Update Formulas:
error = y - y_pred w1 = w1 + (learning_rate * error * x1) w2 = w2 + (learning_rate * error * x2) b = b + (learning_rate * error)

markdown
Copy code

## Example Iteration

Let’s go through an example step by step:

| x1  | x2  | y (label) |
|-----|-----|-----------|
| 0.1 | 0.5 | 1         |
| 0.3 | 0.7 | 1         |
| 0.6 | 0.2 | -1        |
| 0.8 | 0.6 | -1        |

### Initialization
- Initial weights: `w1 = 0.2`, `w2 = 0.4`
- Initial bias: `b = 0.1`
- Learning rate: `0.1`

### Iteration Steps
1. **First Data Point (`x1 = 0.1, x2 = 0.5, y = 1`)**
    - Output: `0.32` → Predicted label: `1` (Correct)
    - No update needed.

2. **Second Data Point (`x1 = 0.3, x2 = 0.7, y = 1`)**
    - Output: `0.5` → Predicted label: `1` (Correct)
    - No update needed.

3. **Third Data Point (`x1 = 0.6, x2 = 0.2, y = -1`)**
    - Output: `0.26` → Predicted label: `1` (Incorrect)
    - Error: `-2`
    - Updated weights: `w1 = 0.08`, `w2 = 0.36`, `b = -0.1`

4. **Fourth Data Point (`x1 = 0.8, x2 = 0.6, y = -1`)**
    - Output: `0.244` → Predicted label: `1` (Incorrect)
    - Error: `-2`
    - Updated weights: `w1 = -0.08`, `w2 = 0.24`, `b = -0.3`

### End of Iteration
- Final weights: `w1 = -0.08`, `w2 = 0.24`
- Final bias: `b = -0.3`

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/jakib01/perceptron-project.git
   cd perceptron-project