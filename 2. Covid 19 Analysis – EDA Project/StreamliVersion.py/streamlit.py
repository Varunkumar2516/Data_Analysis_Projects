import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import streamlit as st

st.set_page_config(layout='wide')
# Data Reading From File 
covid_19=pd.read_csv("../Datasets/covid_19_india.csv")
vaccine_covid=pd.read_csv("../Datasets/covid_vaccine_statewise.csv")


st.sidebar.title("Covid 19 Analysis")
option=st.sidebar.selectbox('SelectOptions',['Data Overview','Overall Analysis','StateWise Analysis','Year Wise Analysis'])


if option=='Data Overview':
    st.markdown(f"""
                <div style ='
                    background-color: #1f1f1f;
                    padding: 20px;
                    border-radius: 15px;
                    text-align: center;
                    color: white;
                    font-size: 24px;
                    font-weight: bold;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                '>
                        Data Overview 
                        </div>""",unsafe_allow_html=True)

    st.subheader("Covid 19 (India) Dataset")
    st.dataframe(covid_19)
    col1,col2=st.columns(2)
    with col1:
        st.markdown("### DataSet Size")
    with col2:
        st.markdown(f"""
                <div style ='
                    background-color: #1f1f1f;
                    padding: 20px;
                    border-radius: 15px;
                    text-align: center;
                    color: white;
                    font-size: 24px;
                    font-weight: bold;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                '>
                        No Investment Records
                        </div>""",unsafe_allow_html=True)
    

    st.subheader("Covid 19 (India) Vaccine DataSet")
    st.dataframe(vaccine_covid)