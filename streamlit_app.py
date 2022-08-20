import streamlit as st
import polars as pl
import datetime

from src.etl import clean, load_from_url
from src.aggregate import simple_agg

#df_path = "./rent.csv"
df_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-07-05/rent.csv"
df_raw = load_from_url(url=df_url)
df_clean = clean(df=df_raw)

add_sidebar = st.sidebar.selectbox(
    "Menu",
    (
        "Aggregate",
        "Individual",
        "Map",
        "Time"
    )
)

if add_sidebar == "Aggregate":
    #st.write("Aggegate")
    df_agg = simple_agg(df=df_clean)
    dict_agg = df_agg.to_dict(as_series=False)
    
    columns = st.columns(3) * 2
    keys = dict_agg.keys()
    values = dict_agg.values()
    data = zip(columns, keys, values)
    for col, key, value in data:
        t_value = value[0]
        if isinstance(t_value, datetime.date):
            col.metric(key, str(t_value))
        else:
            col.metric(key, t_value)

elif add_sidebar == "Individual":
    #county_select = st.selectbox('Pick a County', df_clean.select("county").to_series())
    #city_select = st.selectbox('Pick a City', df_clean.select("city").to_series())
    #nhood_select = st.selectbox('Pick a Neighborhood', df_clean.select("nhood").to_series())
    #slider on price
    st.write("Individual")
elif add_sidebar == "Map":
    st.write("Map")
elif add_sidebar == "Time":
    st.write("Time")
else:
    raise(NotImplementedError)