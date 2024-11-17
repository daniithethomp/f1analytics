import joblib
import pandas as pd

model = joblib.load('trained_model.pkl')

def predict_winner(driver1_id, driver2_id, model=model):
    drivers = pd.read_csv('drivers_power_rankings.csv')
    print(drivers)
    driver1_features = drivers[drivers['driverId'] == driver1_id].drop(columns=['driverId', 'Full Name']).values.flatten()
    driver2_features = drivers[drivers['driverId'] == driver2_id].drop(columns=['driverId', 'Full Name']).values.flatten()
    feature_diff = driver1_features - driver2_features
    prediction = model.predict([feature_diff])
    return (driver1_id,feature_diff) if prediction == 1 else (driver2_id,feature_diff)
