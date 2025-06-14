import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("human_trafficking_cleaned.csv")

st.title("ShadowScore: India’s Hidden Crime Index")

selected_year = st.slider("Select Year", int(df['YEAR'].min()), int(df['YEAR'].max()), step=1)
filtered_df = df[df['YEAR'] == selected_year]

state_scores = filtered_df.groupby('STATE')['HTRS'].mean().reset_index().sort_values(by='HTRS', ascending=False)

fig = px.bar(state_scores, x='STATE', y='HTRS', title=f'HTRS by State in {selected_year}', color='HTRS')
st.plotly_chart(fig)

yearly_trend = df.groupby('YEAR')['HTRS'].mean().reset_index()
fig2 = px.line(yearly_trend, x='YEAR', y='HTRS', title='HTRS Trend Over Time')
st.plotly_chart(fig2)

