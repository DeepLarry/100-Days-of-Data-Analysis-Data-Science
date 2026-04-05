"""Basic Python function examples with machine-learning style use cases.

This file is meant as a small learning note. It shows how functions work,
then connects them to common ML ideas like prediction, activation, and loss.
"""


def greet(name):
	"""Return a simple greeting."""
	return f"Hello, {name}!"


def add_numbers(a, b):
	"""Add two numbers."""
	return a + b


def average(values):
	"""Return the mean of a list of numbers."""
	return sum(values) / len(values)


def sigmoid(z):
	"""Sigmoid activation used in ML classification."""
	import math

	return 1 / (1 + math.exp(-z))


def mse(y_true, y_pred):
	"""Mean squared error loss."""
	total = 0
	for true_value, predicted_value in zip(y_true, y_pred):
		total += (true_value - predicted_value) ** 2
	return total / len(y_true)


def linear_predict(x, weight, bias):
	"""Simple linear model prediction: y = wx + b."""
	return weight * x + bias


print("Function Questions with Answers\n")

print("1. What is a function?")
print("Answer: A function is a reusable block of code that performs one task.\n")

print("2. Why do we use functions?")
print("Answer: Functions reduce repeated code and make programs easier to read.\n")

print("3. What does return do?")
print("Answer: return sends a value back from a function to the caller.\n")

print("4. How are functions used in ML?")
print("Answer: ML uses functions for prediction, activation, and loss calculation.\n")

print("--- Example Outputs ---")
print(greet("Deep"))
print("Add 5 + 7 =", add_numbers(5, 7))
print("Average of [10, 20, 30] =", average([10, 20, 30]))

print("\n--- ML Style Use ---")
score = linear_predict(10, weight=2, bias=3)
print("Linear prediction for x=10:", score)
print("Sigmoid of 2:", sigmoid(2))
print("MSE loss:", mse([1, 2, 3], [1.2, 1.9, 3.1]))

# Output example:
# Hello, Deep!
# Add 5 + 7 = 12
# Average of [10, 20, 30] = 20.0
# Linear prediction for x=10: 23
# Sigmoid of 2: 0.8807970779778823
# MSE loss: 0.020000000000000035
