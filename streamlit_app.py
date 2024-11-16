import streamlit as st
import pandas as pd
import dataframes
import jess_functions
import analytics as a 


st.title("F1 Analytics")
st.write("## Driver Stats")
driver = st.selectbox("Driver",
             options=([name for name in (dataframes.drivers_df())['Full Name']]))
d_standings = a.driver_standing_over_time(driver)
st.line_chart(d_standings, x='year', y='position', x_label='Year', y_label='Position')

st.write("## Constructor Stats")
constructor = st.selectbox("Constructor",
             options=([name for name in dataframes.constructors_df['name']]))
c_standings = a.constructor_standings_over_time(constructor)
st.line_chart(c_standings, x='year', y='position', x_label='Year', y_label='Position')
st.write("## Head to Head")

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

