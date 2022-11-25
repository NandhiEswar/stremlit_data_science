import streamlit as st
import numpy as np
import matplotlib.pyplot as plt 

st.write('binomal distributaion')
#status_text = st.sidebar.empty()
# input the integers
perc_heads = st.number_input(label = 'Chance of Coins Landing on Heads', min_value = 0.0, max_value = 1.0, value = .5)

binom =np.random.binomial(1, perc_heads, 1000)
#input it automatically detects wether it was string are integer
graph_title = st.text_input(label='Graph Title')
st.write(graph_title)

list_of_means = []
for i in range(0,1000):
    list_of_means.append(np.random.choice(binom, 100,replace=True).mean())

fig,ax = plt.subplots()
print(list_of_means)
ax = plt.hist(list_of_means)
st.pyplot(fig)

fig2, ax2 = plt.subplots()

ax2 = plt.hist(binom)

st.pyplot(fig2)