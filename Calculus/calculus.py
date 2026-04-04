"""
calculus.py

A beginner-to-advanced calculus guide with code and ML use-cases.

Run this file directly:
	python calculus.py
"""

from __future__ import annotations

import numpy as np


# =========================
# Level 1: Beginner Basics
# =========================
def f_quadratic(x: float) -> float:
	"""Simple function: f(x) = x^2 + 2x + 1."""
	return x**2 + 2 * x + 1


def derivative_analytic_quadratic(x: float) -> float:
	"""Analytic derivative of f(x) = x^2 + 2x + 1 is 2x + 2."""
	return 2 * x + 2


def derivative_numerical(func, x: float, h: float = 1e-5) -> float:
	"""Numerical derivative using central difference."""
	return (func(x + h) - func(x - h)) / (2 * h)


# ==================================
# Level 2: Intermediate (Gradients)
# ==================================
def mse_loss(w: np.ndarray, X: np.ndarray, y: np.ndarray) -> float:
	"""Mean Squared Error for linear regression."""
	preds = X @ w
	return float(np.mean((preds - y) ** 2))


def mse_gradient(w: np.ndarray, X: np.ndarray, y: np.ndarray) -> np.ndarray:
	"""Gradient of MSE wrt weights w."""
	n = X.shape[0]
	preds = X @ w
	return (2 / n) * (X.T @ (preds - y))


def gradient_descent_linear_regression(
	X: np.ndarray,
	y: np.ndarray,
	lr: float = 0.05,
	epochs: int = 300,
) -> tuple[np.ndarray, list[float]]:
	"""Train linear regression with gradient descent."""
	w = np.zeros(X.shape[1])
	history: list[float] = []

	for _ in range(epochs):
		grad = mse_gradient(w, X, y)
		w -= lr * grad
		history.append(mse_loss(w, X, y))

	return w, history


# =========================================
# Level 3: Advanced (Chain Rule in ML)
# =========================================
def sigmoid(z: np.ndarray) -> np.ndarray:
	return 1 / (1 + np.exp(-z))


def binary_cross_entropy(y_true: np.ndarray, y_prob: np.ndarray) -> float:
	eps = 1e-12
	y_prob = np.clip(y_prob, eps, 1 - eps)
	return float(-np.mean(y_true * np.log(y_prob) + (1 - y_true) * np.log(1 - y_prob)))


def train_logistic_regression(
	X: np.ndarray,
	y: np.ndarray,
	lr: float = 0.1,
	epochs: int = 500,
) -> tuple[np.ndarray, float, list[float]]:
	"""
	Binary logistic regression using gradient descent.

	Chain rule result used here:
		dL/dw = X^T (sigmoid(Xw + b) - y) / n
		dL/db = mean(sigmoid(Xw + b) - y)
	"""
	n, d = X.shape
	w = np.zeros(d)
	b = 0.0
	history: list[float] = []

	for _ in range(epochs):
		z = X @ w + b
		y_prob = sigmoid(z)

		error = y_prob - y
		grad_w = (X.T @ error) / n
		grad_b = float(np.mean(error))

		w -= lr * grad_w
		b -= lr * grad_b

		history.append(binary_cross_entropy(y, y_prob))

	return w, b, history


def logistic_accuracy(X: np.ndarray, y: np.ndarray, w: np.ndarray, b: float) -> float:
	probs = sigmoid(X @ w + b)
	preds = (probs >= 0.5).astype(float)
	return float(np.mean(preds == y))


def make_linear_data(n: int = 120, seed: int = 7) -> tuple[np.ndarray, np.ndarray]:
	"""Create synthetic data: y = 4x + noise."""
	rng = np.random.default_rng(seed)
	x = rng.uniform(-2, 2, size=n)
	noise = rng.normal(0, 0.6, size=n)
	y = 4 * x + noise
	X = np.c_[np.ones(n), x]
	return X, y


def make_classification_data(n: int = 180, seed: int = 21) -> tuple[np.ndarray, np.ndarray]:
	"""Create simple separable 2D classification data."""
	rng = np.random.default_rng(seed)
	half = n // 2

	c0 = rng.normal(loc=[-1.2, -1.0], scale=0.6, size=(half, 2))
	c1 = rng.normal(loc=[1.1, 1.3], scale=0.6, size=(n - half, 2))

	X = np.vstack([c0, c1])
	y = np.hstack([np.zeros(half), np.ones(n - half)])
	return X, y


def run_demo() -> None:
	print("=== Level 1: Derivative Basics ===")
	x_point = 3.0
	analytic = derivative_analytic_quadratic(x_point)
	numeric = derivative_numerical(f_quadratic, x_point)
	print(f"f({x_point}) = {f_quadratic(x_point):.4f}")
	print(f"Analytic derivative at x={x_point}: {analytic:.6f}")
	print(f"Numerical derivative at x={x_point}: {numeric:.6f}")

	print("\n=== Level 2: Linear Regression with Gradient Descent ===")
	X_lin, y_lin = make_linear_data()
	w_lin, hist_lin = gradient_descent_linear_regression(X_lin, y_lin)
	print(f"Learned weights [bias, slope]: {w_lin}")
	print(f"Initial MSE: {hist_lin[0]:.4f} | Final MSE: {hist_lin[-1]:.4f}")

	print("\n=== Level 3: Logistic Regression (Chain Rule in Action) ===")
	X_clf, y_clf = make_classification_data()
	w_log, b_log, hist_log = train_logistic_regression(X_clf, y_clf)
	acc = logistic_accuracy(X_clf, y_clf, w_log, b_log)
	print(f"Learned logistic weights: {w_log}, bias: {b_log:.4f}")
	print(f"Initial BCE: {hist_log[0]:.4f} | Final BCE: {hist_log[-1]:.4f}")
	print(f"Training accuracy: {acc * 100:.2f}%")

	print("\nWhat this teaches for ML:")
	print("1) Derivative gives slope of a function at a point.")
	print("2) Gradient tells direction to reduce loss.")
	print("3) Gradient descent updates parameters to learn from data.")
	print("4) Chain rule connects model output to each parameter update.")


if __name__ == "__main__":
	run_demo()
