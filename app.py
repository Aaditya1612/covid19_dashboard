import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """


st.title('PlotitDown -- ***Covid 19***')
st.write('Currently for ***INDIA*** only.')
st.sidebar.title("Feed Info.")
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

@st.cache
def load_data():
    df=pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")
    return df
df = load_data()

visualization = st.sidebar.selectbox('Select a chart type',('Bar chart','Pie chart','Line chart'))
state_select=st.sidebar.selectbox("Select a state",df['State'].unique())
status_select=st.sidebar.radio('Covid-19 patient status (For pie chart only)',('confirmed_cases','active_cases','recovered_cases','death_cases'))
selected_state=df[df['State']==state_select]
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("Developed by Aaditya")
st.markdown("## ** State level analysis **")

def get_total_dataframe(df):
    total_detaframe=pd.DataFrame({'Status':['Confirmed','Recovered','Deaths','Active'],'Number of cases':(df.iloc[0]['Confirmed'],df.iloc[0]['Recovered'],df.iloc[0]['Deaths'],df.iloc[0]['Active'])})
    return total_detaframe

state_total=get_total_dataframe(selected_state)
if visualization=='Bar chart':
    state_total_graph=px.bar(state_total, x='Status',y='Number of cases', labels={'Number of cases':'Number of cases in %s' % (state_select)},color='Status')
    st.plotly_chart(state_total_graph)

elif visualization=='Pie chart':
    if status_select=='confirmed_cases':
        st.title("Total Confirmed cases")
        fig=px.pie(df,values=df['Confirmed'],names=df['State'])
        fig.update_traces(textposition='inside')
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig)
    
    if status_select=='recovered_cases':
        st.title("Total Recovered  cases")
        fig=px.pie(df,values=df['Recovered'],names=df['State'])
        fig.update_traces(textposition='inside')
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig)
    
    if status_select=='active_cases':
        st.title("Total Active cases")
        fig=px.pie(df,values=df['Active'],names=df['State'])
        fig.update_traces(textposition='inside')
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig)
    
    if status_select=='death_cases':
        st.title("Total Death cases")
        fig=px.pie(df,values=df['Deaths'],names=df['State'])
        fig.update_traces(textposition='inside')
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig)

elif visualization=='Line chart':
    fig = px.line(state_total, x='Status',y='Number of cases', labels={'Number of cases':'Number of cases in %s' % (state_select)})
    st.plotly_chart(fig)