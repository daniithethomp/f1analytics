import streamlit as st
import pandas as pd
import dataframes
import analytics as a 

st.title("F1 Analytics")
st.write("## Driver Stats")
driver = st.selectbox("Driver",
             options=([name for name in (dataframes.drivers_df())['Full Name']]))
d_standings = a.driver_standing_over_time(driver)
st.line_chart(d_standings, x='year', y='position')
st.write("## Constructor Stats")
constructor = st.selectbox("Constructor",
             options=([name for name in dataframes.constructors_df['name']]))
c_standings = a.constructor_standings_over_time(constructor)
st.line_chart(c_standings, x='year', y='position')

st.write("## Constructor Results by Circuit")
circuit = st.selectbox("Circuit", options=([name for name in dataframes.circuit_df['name']]))
# column = st.selectbox("Metric", options=([name for name in dataframes.circuit_df.columns]))
results_per_year = a.constructor_results_over_time_per_circuit(constructor, circuit)
st.line_chart(results_per_year, x='year', y='points')

st.write((results_per_year.columns))
year = st.text_input("Year (1950-2020):", "2020")
st.bar_chart(a.constructor_results_across_circuits_over_year(constructor, year), x='name_circuit', y=["points"], y_label=["points (%)"])

st.write("## Head to Head")