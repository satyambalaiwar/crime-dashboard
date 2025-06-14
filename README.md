# ShadowScore: India’s Hidden Crime Index

This project analyzes and visualizes human trafficking data across Indian states using Python. It provides both a static bar chart (Matplotlib/Seaborn) and an interactive dashboard (Streamlit + Plotly).

## Features

- **Data Analysis:** Calculates the average Human Trafficking Risk Score (HTRS) by state and year.
- **Static Visualization:** Generates a bar chart of average HTRS by state using Matplotlib and Seaborn.
- **Interactive Dashboard:** Explore HTRS trends by state and year with an interactive Streamlit app and Plotly charts.

## Dataset

- **Source:** `human_trafficking_cleaned.csv`
- **Columns:**  
  - `STATE`: Name of the Indian state  
  - `YEAR`: Year of data  
  - `HTRS`: Human Trafficking Risk Score  
  - Other columns as present in your dataset

## Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn
- streamlit
- plotly

Install dependencies with:

```sh
pip install pandas matplotlib seaborn streamlit plotly
```

## Usage

### 1. Static Bar Chart (Matplotlib/Seaborn)

Generates a bar chart of average HTRS by state.

```sh
python analyze.py
```

A window will open displaying the bar chart.

### 2. Interactive Dashboard (Streamlit + Plotly)

Launch the interactive dashboard:

```sh
streamlit run app.py
```

- Use the slider to select a year and view the HTRS by state for that year.
- View the HTRS trend over time for all states.

The dashboard will open in your browser.

## Project Structure

```
crime-dashboard/
├── analyze.py
├── app.py
├── cleaning.py
├── human_trafficking_cleaned.csv
├── human_trafficking.csv
├── README.md
└── ...
```

## Screenshots

_Add screenshots of your charts and dashboard here if desired._

## License

MIT License (or your preferred license)

---

**Author:** Satyam Balaiwar  
**Data Source:** [Add your data source or reference here]