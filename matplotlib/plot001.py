"""
Matplotlib Intro + Basic Practice Questions (with answers)

How to run:
1. Install once: pip install matplotlib
2. Run this file: python plot001.py
3. Close each plot window to see the next one.
"""

import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Quick Intro
# Matplotlib is a Python library for drawing graphs like:
# line chart, bar chart, scatter plot, pie chart, and subplots.
# ------------------------------------------------------------


# Question 1:
# Plot a line graph for x=[1,2,3,4] and y=[10,20,25,30].
# Answer:
def q1_line_plot():
	x = [1, 2, 3, 4]
	y = [10, 20, 25, 30]
	plt.figure("Q1: Line Plot")
	plt.plot(x, y, marker="o", color="blue", label="Sales")
	plt.title("Q1: Simple Line Plot")
	plt.xlabel("X values")
	plt.ylabel("Y values")
	plt.grid(True)
	plt.legend()
	plt.show()


# Question 2:
# Create a bar chart for categories A,B,C with values 5,7,3.
# Answer:
def q2_bar_chart():
	categories = ["A", "B", "C"]
	values = [5, 7, 3]
	plt.figure("Q2: Bar Chart")
	plt.bar(categories, values, color=["red", "green", "orange"])
	plt.title("Q2: Bar Chart")
	plt.xlabel("Category")
	plt.ylabel("Value")
	plt.show()


# Question 3:
# Draw a scatter plot using x=[1,2,3,4,5], y=[2,4,1,8,7].
# Answer:
def q3_scatter_plot():
	x = [1, 2, 3, 4, 5]
	y = [2, 4, 1, 8, 7]
	plt.figure("Q3: Scatter Plot")
	plt.scatter(x, y, color="purple", s=80)
	plt.title("Q3: Scatter Plot")
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.grid(True)
	plt.show()


# Question 4:
# Make two subplots: sin-like and cos-like dummy lines.
# Answer:
def q4_subplots():
	x = [0, 1, 2, 3, 4]
	y1 = [0, 1, 0, -1, 0]
	y2 = [1, 0, -1, 0, 1]

	fig, axes = plt.subplots(1, 2, figsize=(10, 4))

	axes[0].plot(x, y1, color="teal")
	axes[0].set_title("Q4: Plot 1")
	axes[0].set_xlabel("X")
	axes[0].set_ylabel("Y")
	axes[0].grid(True)

	axes[1].plot(x, y2, color="brown")
	axes[1].set_title("Q4: Plot 2")
	axes[1].set_xlabel("X")
	axes[1].set_ylabel("Y")
	axes[1].grid(True)

	fig.tight_layout()
	plt.show()


# Question 5:
# Create a pie chart for [40, 35, 25] with labels ["Python", "Java", "C++"].
# Answer:
def q5_pie_chart():
	sizes = [40, 35, 25]
	labels = ["Python", "Java", "C++"]
	plt.figure("Q5: Pie Chart")
	plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
	plt.title("Q5: Pie Chart")
	plt.axis("equal")
	plt.show()


if __name__ == "__main__":
	q1_line_plot()
	q2_bar_chart()
	q3_scatter_plot()
	q4_subplots()
	q5_pie_chart()
