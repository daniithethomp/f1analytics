import streamlit as st
import pandas as pd
import dataframes
import altair as alt

def driver_standing_over_time(driver):
    drivers_df = dataframes.drivers_df()
    driver_id = (drivers_df)[drivers_df['Full Name'] == driver]['driverId'].iloc[0]
    driver_standing_frame = dataframes.driver_standings_df
    driver_specific_standings = driver_standing_frame[driver_standing_frame['driverId'] == driver_id]
    driver_specific_standings = driver_specific_standings.join(dataframes.races_df(), on='raceId', lsuffix='l', rsuffix='r')
    driver_standing_per_year = driver_specific_standings.loc[driver_specific_standings.groupby('year')['round'].idxmax()]
    return driver_standing_per_year

def constructor_standings_over_time(constructor):
    constructor_df = dataframes.constructors_df
    constructor_id = (constructor_df)[constructor_df['name'] == constructor]['constructorId'].iloc[0]
    constructor_standing_frame = dataframes.constructor_standings_df
    constructor_specific_standings = constructor_standing_frame[constructor_standing_frame['constructorId'] == constructor_id]
    constructor_specific_standings = constructor_specific_standings.join(dataframes.races_df(), on='raceId', lsuffix='l', rsuffix='r')
    constructor_standing_per_year = constructor_specific_standings.loc[constructor_specific_standings.groupby('year')['round'].idxmax()]
    return constructor_standing_per_year

st.title("F1 Growth Thing Name")
st.write("## Driver Stats")
driver = st.selectbox("Driver",
             options=([name for name in (dataframes.drivers_df())['Full Name']]))
d_standings = driver_standing_over_time(driver)
st.line_chart(d_standings, x='year', y='position')
st.write("## Constructor Stats")
constructor = st.selectbox("Constructor",
             options=([name for name in dataframes.constructors_df['name']]))
c_standings = constructor_standings_over_time(constructor)
st.line_chart(c_standings, x='year', y='position')
st.write("## Head to Head")

