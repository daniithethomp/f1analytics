import dataframes

def best_pit_stop_per_race(race):
    pit_stops = dataframes.pit_stop_df[dataframes.pit_stop_df['Race Identifier'] == race]
    best_pit_stop = dataframes.pit_stop_df.loc[pit_stops['time'].idxmin()]
    return best_pit_stop

    

 

    