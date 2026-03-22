"""Interactive Streamlit dashboard using Matplotlib.

Run with:
	streamlit run plot002.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def build_data(num_points: int, frequency: float, noise: float, seed: int) -> pd.DataFrame:
	"""Create synthetic signal data for plotting."""
	rng = np.random.default_rng(seed)
	x = np.linspace(0, 10, num_points)
	base = np.sin(frequency * x)
	y = base + rng.normal(0, noise, num_points)
	return pd.DataFrame({"x": x, "y": y, "base": base})


def render_plot(data: pd.DataFrame, chart_type: str, color: str) -> plt.Figure:
	"""Render the selected chart type as a Matplotlib figure."""
	fig, ax = plt.subplots(figsize=(10, 5))

	if chart_type == "Line":
		ax.plot(data["x"], data["y"], color=color, linewidth=2, label="Signal")
	elif chart_type == "Scatter":
		ax.scatter(data["x"], data["y"], color=color, s=35, alpha=0.8, label="Points")
	elif chart_type == "Bar":
		sample = data.iloc[: min(40, len(data))]
		ax.bar(sample["x"], sample["y"], color=color, width=0.2, alpha=0.85, label="Bars")
	elif chart_type == "Histogram":
		ax.hist(data["y"], bins=20, color=color, alpha=0.85, edgecolor="black", label="Distribution")
		ax.set_xlabel("Signal Value")
		ax.set_ylabel("Count")

	if chart_type != "Histogram":
		ax.set_xlabel("X")
		ax.set_ylabel("Y")

	ax.set_title(f"{chart_type} Visualization")
	ax.grid(True, linestyle="--", alpha=0.4)
	ax.legend(loc="best")
	fig.tight_layout()
	return fig


def main() -> None:
	st.set_page_config(page_title="Dynamic Matplotlib Visualizer", layout="wide")

	st.title("Dynamic Data Visualizer")
	st.write("Use the controls to generate and explore an interactive Matplotlib chart.")

	st.sidebar.header("Controls")
	chart_type = st.sidebar.selectbox("Chart Type", ["Line", "Scatter", "Bar", "Histogram"])
	num_points = st.sidebar.slider("Number of Points", min_value=20, max_value=500, value=150, step=10)
	frequency = st.sidebar.slider("Wave Frequency", min_value=0.2, max_value=4.0, value=1.2, step=0.1)
	noise = st.sidebar.slider("Noise", min_value=0.0, max_value=1.0, value=0.2, step=0.05)
	seed = st.sidebar.number_input("Random Seed", min_value=0, max_value=9999, value=7, step=1)
	color = st.sidebar.color_picker("Plot Color", "#1f77b4")

	data = build_data(num_points=num_points, frequency=frequency, noise=noise, seed=int(seed))
	fig = render_plot(data=data, chart_type=chart_type, color=color)

	col1, col2 = st.columns([2, 1])
	with col1:
		st.pyplot(fig, clear_figure=True)
	with col2:
		st.subheader("Summary")
		st.metric("Mean", f"{data['y'].mean():.3f}")
		st.metric("Std Dev", f"{data['y'].std():.3f}")
		st.metric("Max", f"{data['y'].max():.3f}")
		st.metric("Min", f"{data['y'].min():.3f}")

	st.subheader("Data Preview")
	st.dataframe(data.head(15), use_container_width=True)

	csv_data = data.to_csv(index=False).encode("utf-8")
	st.download_button(
		label="Download CSV",
		data=csv_data,
		file_name="dynamic_plot_data.csv",
		mime="text/csv",
	)


if __name__ == "__main__":
	main()
