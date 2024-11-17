import joblib
import pandas as pd
import dataframes as df

drivers = df.drivers_df()
drivers = drivers[['driverId','Full Name']]
results = df.results_df
wins = results[results['positionOrder'] == 1]
podiums = results[results['positionOrder'] <= 3]
wins = wins.groupby('driverId').size().reset_index(name='wins')
podiums = podiums.groupby('driverId').size().reset_index(name='podiums')
drivers = drivers.merge(podiums, on='driverId', how='left')
drivers = drivers.merge(wins, on='driverId', how='left')
drivers['wins'] = drivers['wins'].fillna(0)
drivers['podiums'] = drivers['podiums'].fillna(0)
championships = df.driver_standings_df
championships = championships.join(df.races_df(), on='raceId', lsuffix='l', rsuffix='r')
championships = championships[championships['position'] == 1]
championships = championships.loc[championships.groupby('year')['round'].idxmax()]
drivers['championships'] = championships.groupby('driverId').size().reset_index(name='championships')['championships']
drivers['championships'] = drivers['championships'].fillna(0)
# points = results.groupby('driverId')['points'].sum().reset_index(name='points')
# drivers = drivers.merge(points, on='driverId', how='left')

qualifying_results = df.qualifying_results_df
pole_positions = qualifying_results[qualifying_results['position'] == 1]
pole_positions = pole_positions.groupby('driverId').size().reset_index(name='pole_positions')
drivers = drivers.merge(pole_positions, on='driverId', how='left')
drivers['pole_positions'] = drivers['pole_positions'].fillna(0)

finish_positions_vs_start = results[['driverId', 'grid', 'positionOrder']]
finish_positions_vs_start['positionDiff'] = finish_positions_vs_start['grid'] - finish_positions_vs_start['positionOrder']
average_position_diff = finish_positions_vs_start.groupby('driverId')['positionDiff'].mean().reset_index(name='average_position_diff')
drivers = drivers.merge(average_position_diff, on='driverId', how='left')

fastest_laps = results[results['fastestLapTime'].notnull()]
fastest_laps = fastest_laps.groupby('raceId')['fastestLapTime'].min()
fastest_laps = fastest_laps.reset_index().merge(results[['raceId', 'driverId', 'fastestLapTime']], on=['raceId', 'fastestLapTime'])
drivers = drivers.merge(fastest_laps.groupby('driverId').size().reset_index(name='fastest_laps'), on='driverId', how='left')
drivers['fastest_laps'] = drivers['fastest_laps'].fillna(0)

def predict_winner(driver1_id, driver2_id, drivers, model):
    driver1_features = drivers[drivers['driverId'] == driver1_id].drop(columns=['driverId', 'Full Name']).values.flatten()
    driver2_features = drivers[drivers['driverId'] == driver2_id].drop(columns=['driverId', 'Full Name']).values.flatten()
    feature_diff = driver1_features - driver2_features
    print(feature_diff)
    prediction = model.predict([feature_diff])
    return driver1_id if prediction == 1 else driver2_id

model = joblib.load('trained_model.pkl')

print(predict_winner(1, 855, drivers, model))