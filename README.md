# F1 Analytics

A Streamlit application for analysing Formula 1 race data.

## Features

- **Driver Stats**: View driver standings and wins per season.
- **Constructor Stats**: View constructor standings per season + other features Andrew has added.
- **Head to Head**: Put two drivers against each other and let our model predict who would win
- **Race Stats**: View results, fastest lap times, and fastest pit stops for selected races.

### The Model
#### Feature Selection
The features were selected manually using intuition.

The features we selected are:
- number of races won
- number of podiums
- number of championships won
- average position gain in races
- number of fastest laps
#### Model Training
For each race, we created pairs of each driver in the race. We then calculated the difference between each of the driver's selected features. We labelled the data with which driver finished ahead of the other in the race.

This data was then split into two, with half being the training data and half being the test data.
A Logistic Regression model was then trained and packaged.
#### Model Testing
The model's statistics:

- Accuracy: 0.648
- Precision: 0.648
- Recall: 0.720
- F1 Score: 0.682
#### Using the model
The selected features of each driver was written to `driver_power_rankings.csv` and is used to quickly read the features for the selected drivers. The feature difference is calculated and fed into the model which then returns a prediction of who would win.

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


