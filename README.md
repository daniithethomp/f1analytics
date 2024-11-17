# F1 Analytics

A Streamlit application for analysing Formula 1 race data.

## Features

- **Driver Stats**: View driver standings and wins per season.
- **Constructor Stats**: View constructor standings per season + other features Andrew has added.
- **Head to Head**: Put two drivers against each other to see who comes out ahead.
- **Race Stats**: View results, fastest lap times, and fastest pit stops for selected races.

### How to run it on your own machine

1. **Clone the repository**

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run streamlit_app.py
    ```

## Data Sources

The data used in this application is sourced from [Kaggle - Formula 1 World Championship (1950 - 2024), rohanrao](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/data)


