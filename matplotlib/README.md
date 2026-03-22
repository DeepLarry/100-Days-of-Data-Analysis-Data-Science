# Dynamic Matplotlib + Streamlit Visualizer

An interactive visualization app built with **Streamlit** and **Matplotlib**.
You can change chart type, signal frequency, noise, number of points, random seed, and plot color in real time.

## Features

- Dynamic chart controls from the sidebar
- Multiple chart types: Line, Scatter, Bar, Histogram
- Real-time summary metrics (mean, std dev, max, min)
- Data preview table
- CSV download for generated data

## Project Structure

- `plot001.py` - Basic matplotlib practice examples
- `plot002.py` - Interactive Streamlit dashboard
- `requirements.txt` - Python dependencies

## Setup

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run plot002.py
```

Then open the local URL shown in terminal (usually `http://localhost:8501`).

## Share on GitHub

1. Create a new repository on GitHub.
2. Push this project:

```bash
git init
git add .
git commit -m "Add dynamic matplotlib streamlit visualizer"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Optional: Deploy Online

You can deploy this app free using **Streamlit Community Cloud**:

1. Push code to GitHub.
2. Go to https://share.streamlit.io
3. Connect your GitHub repo and deploy `plot002.py`.
