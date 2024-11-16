import dataframes as df

def driver_standing_over_time(driver):
    drivers_df = df.drivers_df()
    driver_id = (drivers_df)[drivers_df['Full Name'] == driver]['driverId'].iloc[0]
    driver_standing_frame = df.driver_standings_df
    driver_specific_standings = driver_standing_frame[driver_standing_frame['driverId'] == driver_id]
    driver_specific_standings = driver_specific_standings.join(df.races_df(), on='raceId', lsuffix='l', rsuffix='r')
    driver_standing_per_year = driver_specific_standings.loc[driver_specific_standings.groupby('year')['round'].idxmax()]
    return driver_standing_per_year

def constructor_standings_over_time(constructor):
    constructor_df = df.constructors_df
    constructor_id = (constructor_df)[constructor_df['name'] == constructor]['constructorId'].iloc[0]
    constructor_standing_frame = df.constructor_standings_df
    constructor_specific_standings = constructor_standing_frame[constructor_standing_frame['constructorId'] == constructor_id]
    constructor_specific_standings = constructor_specific_standings.join(df.races_df(), on='raceId', lsuffix='l', rsuffix='r')
    constructor_standing_per_year = constructor_specific_standings.loc[constructor_specific_standings.groupby('year')['round'].idxmax()]
    return constructor_standing_per_year

def driver_wins_over_time(driver):
    drivers_df = df.drivers_df()
    driver_id = (drivers_df)[drivers_df['Full Name'] == driver]['driverId'].iloc[0]
    driver_wins_frame = df.driver_standings_df
    driver_specific_wins = driver_wins_frame[driver_wins_frame['driverId'] == driver_id]
    driver_specific_wins = driver_specific_wins.join(df.races_df(), on='raceId', lsuffix='l', rsuffix='r')
    driver_wins_per_year = driver_specific_wins[driver_specific_wins['position'] == 1].groupby('year').size()
    return driver_wins_per_year

results = df.results_df
fastest_laps = results[results['fastestLapTime'].notnull()]
fastest_laps = fastest_laps.groupby('raceId')['fastestLapTime'].min()