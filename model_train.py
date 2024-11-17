import pandas as pd
import dataframes as df
import analytics as a

# Useful data
# Wins
# Championships
# Podiums
# average Positions gained
# Points
# Fastest laps
# Pole positions

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

print(drivers)

def create_driver_pairs(race_results, drivers):
    pairs = []
    for race_id in race_results['raceId'].unique():
        race_drivers = race_results[race_results['raceId'] == race_id]['driverId'].values
        for i in range(len(race_drivers)):
            for j in range(len(race_drivers)):
                driver1 = race_drivers[i]
                driver2 = race_drivers[j]
                driver1_features = drivers[drivers['driverId'] == driver1].drop(columns=['driverId','Full Name']).values.flatten()
                driver2_features = drivers[drivers['driverId'] == driver2].drop(columns=['driverId','Full Name']).values.flatten()
                feature_diff = driver1_features - driver2_features
                res = race_results[race_results['raceId'] == race_id]
                # print(int(res[res['driverId'] == driver1]['positionOrder'].values[0]))
                # print(int(res[res['driverId'] == driver2]['positionOrder'].values[0]))
                winner = 1 if int(res[res['driverId'] == driver1]['positionOrder'].values[0]) <= int(res[res['driverId'] == driver2]['positionOrder'].values[0]) else 2
                # print(winner)
                pairs.append(list(feature_diff) + [winner])
    return pd.DataFrame(pairs, columns=['podiums','wins','championships','pole_positions','average_position_diff','fastest_laps'] + ['winner'])

time_start = pd.Timestamp.now()
race_results = df.results_df[df.results_df['raceId'] < 1000][['raceId','driverId','positionOrder']]
print(race_results)
pairs = create_driver_pairs(race_results, drivers)
time_fin = pd.Timestamp.now()
print("Time taken:", (time_fin - time_start))
X = pairs.drop(columns=['winner'])
Y = pairs['winner']
print(pairs[pairs['winner'] == 1].shape)
print(pairs[pairs['winner'] == 2].shape)
print(pairs.shape)

X_train = X[0::2]
Y_train = Y[0::2]
X_test = X[1::2]
Y_test = Y[1::2]

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
accuracy = accuracy_score(Y_test, y_pred)
precision = precision_score(Y_test, y_pred)
recall = recall_score(Y_test, y_pred)
f1 = f1_score(Y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')

def predict_winner(driver1_id, driver2_id, drivers, model):
    driver1_features = drivers[drivers['driverId'] == driver1_id].drop(columns=['driverId', 'Full Name']).values.flatten()
    driver2_features = drivers[drivers['driverId'] == driver2_id].drop(columns=['driverId', 'Full Name']).values.flatten()
    feature_diff = driver1_features - driver2_features
    print(feature_diff)
    prediction = model.predict([feature_diff])
    return driver1_id if prediction == 1 else driver2_id

import joblib

joblib.dump(model, 'trained_model.pkl')