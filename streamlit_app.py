import streamlit as st
import pandas as pd

st.title(' 🚀 Machine Learning Application')

st.info(" This app builds a machine learning model! ")


with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/streamlit_freecodecamp/d44c4c1320f8417b3d5494902e5366b715314528/app_8_classification_penguins/penguins_cleaned.csv')
  df



