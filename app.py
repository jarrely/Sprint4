import streamlit as st # type: ignore
import pandas as pd
import math as mt
import numpy as np
import plotly.express as px
vehicles=pd.read_csv("/Notebooks/vehicles_us.csv",sep=',')

st.header("TripleTen Sprint 4 App", divider=True)
#fig1= px.scatter(vehiclesv2, x='model_year', y='price', color='type')
#fig1.update_layout(title_text= 'Median Price by Vehicle Type and Model Year', xaxis_title='Model Year', yaxis_title='Median Price')
#fig1.show()
