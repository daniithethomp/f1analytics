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



# Andrews Functions ====================================================================================================

def get_constructor_id(constructor_name):
    return (df.constructors_df)[df.constructors_df['name'] == constructor_name]['constructorId'].iloc[0]


def get_circuit_id(circuit_name):
    return (df.circuit_df)[df.circuit_df['name'] == circuit_name]['circuitId'].iloc[0]

# Will get the points earned by a constructor (at a given circuit) over time
def constructor_results_over_time_per_circuit(constructor_name, circuit_name):
    # Get all race results for that constructor
    results = df.constructor_results_df[df.constructor_results_df['constructorId'] == get_constructor_id(constructor_name)]
    
    # Join race table so can query year, then filter by circuit
    results = results.join(df.races_df(), on='raceId', lsuffix='', rsuffix='_race')
    results = results[results['circuitId'] == get_circuit_id(circuit_name)]

    # Join circuit stats
    results = results.join(df.circuit_df, on='circuitId', lsuffix='', rsuffix='_circuit')

    # Race results for that race, and that constructor
    constructor_results_per_year = results.loc[results.groupby('year')['round'].idxmax()]
    return constructor_results_per_year

def convert_column_to_percent(column_name, dataframe, negate=False):
    max_val = dataframe.loc[dataframe[column_name].idxmax()]
    dataframe.assign(Percentage = lambda x: (x[column_name] /max_val * 100))
    return dataframe

# will get the points earned by a constructor over that year
def constructor_results_across_circuits_over_year(constructor_name, year):
    # Get all race results for that constructor
    results = df.constructor_results_df[df.constructor_results_df['constructorId'] == get_constructor_id(constructor_name)]

    # Join race table to query year, then filter by year
    results = results.join(df.races_df(), on='raceId', lsuffix='', rsuffix='_race')

    results = results[results['year'] == year]

    # Join circuit stats
    results = results.join(df.circuit_df, on='circuitId', lsuffix='', rsuffix='_circuit')

    # Race results for that race, and that constructor
    constructor_results_per_year = results.sort_values("round")
    # constructor_results_per_year = convert_column_to_percent("points", constructor_results_per_year)
    # constructor_results_per_year = convert_column_to_percent("alt", constructor_results_per_year, True)
    return constructor_results_per_year
