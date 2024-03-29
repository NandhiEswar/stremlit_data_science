import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

st.title('reading the data with pandas')
test = st.file_uploader('select file upload ')
st.write(pd.DataFrame(test))
data = pd.read_csv('penguins.csv')

st.write(data.head(50))
st.stop()
st.title("Palmer's Penguins")

st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

selected_species = st.selectbox('What species would you like to visualize?',['Adelie', 'Gentoo', 'Chinstrap'])

selected_x_var = st.selectbox('What do want the x variable to be?',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

selected_y_var = st.selectbox('What about the y?',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

enguins_df = data[data['species'] == selected_species]
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data=data,x = data[selected_x_var], y = data[selected_y_var],hue ='species',markers=markers)
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
st.pyplot(fig)