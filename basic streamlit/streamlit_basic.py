import streamlit as st 
import time
import numpy as np 

#install the process bar
progress_bar = st.sidebar.progress(0)
st.title('random variabile ')
# writing the text 
st.write('scateer plot')
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)

chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    #this time is help to view in perfect
    time.sleep(0.06)
    #print(i)

#progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since

# this button is not connected to any other logic, it just causes a plain

# rerun.
#button 
st.button("Re-run")