import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Data visilization ')

st.write('This app analyses trees in San Francisco using' ' a dataset kindly provided by SF DPW')

tree_df = pd.read_csv('trees.csv')

st.write(tree_df.head())

df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
#multi charts are in present 
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)
#adding the new column to the data
df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped)) * 500
st.line_chart(df_dbh_grouped)

tree_data = tree_df.dropna(subset=['longitude','latitude'])

tree_data = tree_df.sample(n=100)
#print(tree_data)
st.map(tree_data)

#streamlit config show 
#set the conifigration files


