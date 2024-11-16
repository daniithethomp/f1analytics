import pandas as pd
import kagglehub

path = kagglehub.dataset_download("rohanrao/formula-1-world-championship-1950-2020")

print("Path to dataset files:", path)

driver_standings_df = pd.read_csv(path + "/driver_standings.csv")

def drivers_df():
    dataframe = pd.read_csv(path + "/drivers.csv")
    dataframe['Full Name'] = dataframe['forename'] + " " + dataframe['surname']
    return dataframe

races_df =  pd.read_csv(path + "/races.csv")