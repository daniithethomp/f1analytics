import dataframes
import pandas as pd


def best_pit_stop_per_race(race):
    raceId = (dataframes.races_df())[(dataframes.races_df())['Race Identifier'] == race]['raceId'].iloc[0]
    raceRow = dataframes.pit_stop_df[dataframes.pit_stop_df['raceId'] == raceId]
    if raceRow.empty:
        raise Exception("No pit stops recorded")
    else:
        best_pit_stop = raceRow.groupby('raceId')['milliseconds'].idxmin()
        return best_pit_stop
 
def lap_times(race):
    raceId = (dataframes.races_df())[(dataframes.races_df())['Race Identifier'] == race]['raceId'].iloc[0]
    raceRow = dataframes.lap_times_df[dataframes.lap_times_df['raceId'] == raceId]
    if raceRow.empty:
        raise Exception("No lap times recorded")
    else:
        best_lap_time = raceRow.groupby('raceId')['milliseconds'].idxmin()
        return best_lap_time