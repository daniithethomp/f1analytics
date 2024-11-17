import pandas as pd
import kagglehub
path = kagglehub.dataset_download("rohanrao/formula-1-world-championship-1950-2020")

print("Path to dataset files:", path)

driver_standings_df = pd.read_csv(path + "/driver_standings.csv")

def drivers_df():
    dataframe = pd.read_csv(path + "/drivers.csv")
    dataframe['Full Name'] = dataframe['forename'] + " " + dataframe['surname']
    return dataframe

def races_df(ascending=True):
    dataframe =  pd.read_csv(path + "/races.csv")
    dataframe = dataframe[dataframe['raceId'] != 355]
    dataframe['Race Identifier'] = dataframe['year'].astype('str') + " " + dataframe['name']
    dataframe = dataframe.sort_values(by='year', ascending=ascending)
    return dataframe

def races_df_unsorted():
    dataframe = pd.read_csv(path + "/races.csv")
    dataframe = dataframe[dataframe['raceId'] != 355]
    dataframe['year'] = dataframe['year'].astype(str)
    return dataframe

pit_stop_df = pd.read_csv(path + "/pit_stops.csv")

lap_times_df = pd.read_csv(path + "/lap_times.csv")

results_df = pd.read_csv(path + "/results.csv")
qualifying_results_df = pd.read_csv(path + "/qualifying.csv")

constructor_standings_df = pd.read_csv(path + "/constructor_standings.csv")
constructors_df = pd.read_csv(path + "/constructors.csv")

constructor_results_df = pd.read_csv(path + "/constructor_results.csv")

circuit_df = pd.read_csv(path + "/circuits.csv").sort_values('name')