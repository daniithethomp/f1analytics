import streamlit as st
import pandas as pd
import dataframes
import jess_functions
import analytics as a 
from model_test import predict_winner


st.title("F1 Analytics")
st.write("## Driver Stats")
driver = st.selectbox("Driver",
             options=([name for name in (dataframes.drivers_df())['Full Name']]))
st.write("### Driver Standing Per Season")
d_standings = a.driver_standing_over_time(driver)
st.line_chart(d_standings, x='year', y='position', x_label='Year', y_label='Position')
st.write("### Driver Wins Per Season")
st.line_chart(a.driver_wins_over_time(driver))

st.write("## Constructor Stats")
constructor = st.selectbox("Constructor",
             options=([name for name in dataframes.constructors_df['name']]))
st.write("### Constructor Standing Per Season")
c_standings = a.constructor_standings_over_time(constructor)
st.line_chart(c_standings, x='year', y='position', x_label='Year', y_label='Position')
st.write("## Head to Head")
driver1 = st.selectbox("Driver 1",
                       options=([name for name in (dataframes.drivers_df())['Full Name']]))
driver2 = st.selectbox("Driver 2",
                          options=([name for name in (dataframes.drivers_df())['Full Name']]))
driver1id = dataframes.drivers_df()[dataframes.drivers_df()['Full Name'] == driver1]['driverId'].values[0]
driver2id = dataframes.drivers_df()[dataframes.drivers_df()['Full Name'] == driver2]['driverId'].values[0]
results, feature_diff = predict_winner(driver1id, driver2id)
st.write("Our model predicts that:")
st.write(driver1 if results == 1 else driver2)
st.write("will win against")
st.write(driver2 if results == 1 else driver1)
st.write("### Feature Difference")
st.write(pd.DataFrame([feature_diff], columns=['podiums','wins','championships','pole_positions','average_position_diff','fastest_laps']))
st.write("## All Races")
sort_order = st.radio("Order:",("Ascending", "Descending"))
ascending = True if sort_order == "Ascending" else False
race = st.selectbox("Race", 
                options=([race for race in (dataframes.races_df(ascending=ascending))['Race Identifier']]))

st.write("### Fastest Lap Time")
try:
    best_lap_time = jess_functions.lap_times(race)
    st.dataframe(best_lap_time)
except Exception as e:
    st.write(str(e))

# st.write("### Fastest Pit Stop (ms)")
# st.write("This data includes drive-through penalties")
# try:
#     best_pit_stop = jess_functions.best_pit_stop_per_race(race)
#     st.dataframe(best_pit_stop)
# except Exception as e:
#     st.write(str(e))

