import streamlit as st
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohanrao/formula-1-world-championship-1950-2020")

print("Path to dataset files:", path)

df_drivers = pd.read_csv(path + "/drivers.csv")
df_drivers['full_name'] = df_drivers['forename'] + " " + df_drivers['surname']
print(df_drivers['full_name'])

st.title("F1 Growth Thing Name")
st.selectbox("Drivers",
             options=([name for name in df_drivers['full_name']]))
st.write(
    ""
)