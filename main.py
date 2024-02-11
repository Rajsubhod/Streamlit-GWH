import streamlit as st
import pandas as pd
import numpy as np
import csv

st.title('Pokemon Data Visualisation Tool')

@st.cache_data
def load_data():
    data = pd.read_csv('pokemon.csv')
    return data

data = load_data()

# create a dataframe eith the pokemon data
df = pd.DataFrame(data)

# display the dataframe
st.dataframe(df)