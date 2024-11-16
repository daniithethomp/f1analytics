import pandas as pd
import kagglehub
import json
from urllib.request import urlopen

response = urlopen('https://api.openf1.org/v1/pit?')
data = json.loads(response.read().decode('utf-8'))

path = kagglehub.dataset_download("rohanrao/formula-1-world-championship-1950-2020")

print("Path to dataset files:", path)

driver_standings_df = pd.read_csv(path + "/driver_standings.csv")

def drivers_df():
    dataframe = pd.read_csv(path + "/drivers.csv")
    dataframe['Full Name'] = dataframe['forename'] + " " + dataframe['surname']
    return dataframe

def races_df(ascending=True):
    dataframe =  pd.read_csv(path + "/races.csv")
    dataframe['Race Identifier'] = dataframe['year'].astype('str') + " " + dataframe['name']
    dataframe = dataframe.sort_values(by='year', ascending=ascending)
    return dataframe

pit_stop_df = pd.read_csv(path + "/pit_stops.csv")

lap_times_df = pd.read_csv(path + "/lap_times.csv")

constructor_standings_df = pd.read_csv(path + "/constructor_standings.csv")
constructors_df = pd.read_csv(path + "/constructors.csv")

