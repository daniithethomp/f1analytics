import streamlit as st
import pandas as pd
import dataframes as df
import analytics as a 
from model_test import predict_winner


st.title("F1 Analytics")
st.write("## Driver Stats")
driver = st.selectbox("Driver",
             options=([name for name in (df.drivers_df())['Full Name']]))
st.write("### Driver Standing Per Season")
d_standings = a.driver_standing_over_time(driver)
st.line_chart(d_standings, x='year', y='position', x_label='Year', y_label='Position')
st.write("### Driver Wins Per Season")
st.line_chart(a.driver_wins_over_time(driver))

st.write("## Constructor Stats")
constructor = st.selectbox("Constructor",
             options=([name for name in df.constructors_df['name']]))
st.write("### Constructor Standing Per Season")
c_standings = a.constructor_standings_over_time(constructor)
st.line_chart(c_standings, x='year', y='position', x_label='Year', y_label='Position')

st.write("### Constructor Results by Circuit")
circuit = st.selectbox("Circuit", options=([name for name in df.circuit_df['name']]))
results_per_year = a.constructor_results_over_time_per_circuit(constructor, circuit)
st.line_chart(results_per_year, x='year', y='points')

st.write("### Constructor Results Over Season")
year = st.text_input("Year (1950-2020):", "2020")
st.bar_chart(a.constructor_results_across_circuits_over_year(constructor, year), x='name_circuit', y="points", x_label="circuit name")

st.write("## Head to Head")
driver1 = st.selectbox("Driver 1",
                       options=([name for name in (df.drivers_df())['Full Name']]))
driver2 = st.selectbox("Driver 2",
                          options=([name for name in (df.drivers_df())['Full Name']]))
driver1id = df.drivers_df()[df.drivers_df()['Full Name'] == driver1]['driverId'].values[0]
driver2id = df.drivers_df()[df.drivers_df()['Full Name'] == driver2]['driverId'].values[0]
results, feature_diff = predict_winner(driver1id, driver2id)
st.write("Our model predicts that:")
st.write(driver1 if results == 1 else driver2)
st.write("will win against")
st.write(driver2 if results == 1 else driver1)
st.write("### Feature Difference")
st.write(pd.DataFrame([feature_diff], columns=['podiums','wins','championships','pole_positions','average_position_diff','fastest_laps']))
st.write("### Model Accuracy")
st.write("Our model has an accuracy of 65%")
st.write("## All Races")


# Separate Race Information

st.write("## Race Stats")
sort_order = st.radio("Order:",("Ascending", "Descending"))
ascending = True if sort_order == "Ascending" else False
race = st.selectbox("Race", 
                options=([race for race in (df.races_df(ascending=ascending))['Race Identifier']]))

st.write("### Race Results")
try:
    race_results_df = a.race_results(race)
    st.table(race_results_df)
except Exception as e:
    st.write(str(e))

st.write("#### Fastest Lap Time")
try:
    best_lap_time = a.lap_times(race)
    st.table(best_lap_time)
except Exception as e:
    st.write(str(e))

st.write("#### Fastest Pit Stop (seconds)")
st.write("This data includes drive-through penalties")
try:
    best_pit_stop = a.best_pit_stop_per_race(race)
    st.table(best_pit_stop)
except Exception as e:
    st.write(str(e))
