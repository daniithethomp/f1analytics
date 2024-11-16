import streamlit as st
import pandas as pd
import dataframes

def driver_standing_over_time(driver):
    drivers_df = dataframes.drivers_df()
    driver_id = (drivers_df)[drivers_df['Full Name'] == driver]['driverId'].iloc[0]
    print(driver_id)
    driver_standing_frame = dataframes.driver_standings_df
    driver_specific_standings = driver_standing_frame[driver_standing_frame['driverId'] == driver_id]
    return driver_specific_standings

st.title("F1 Growth Thing Name")
st.write("## Driver Stats")
driver = st.selectbox("Driver",
             options=([name for name in (dataframes.drivers_df())['Full Name']]))
standings = driver_standing_over_time(driver)
st.dataframe(standings)
st.write("## Constructor Stats")
st.selectbox("Constructor",
             options=())
st.write("## Head to Head")

