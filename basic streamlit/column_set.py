#this removed to st.beta_columns() , chaged to st.columns()
#st.color_picker()
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd 

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

image = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json')

st_lottie(image, speed=1.0, width=800, height=400)


st.title('learning')
st.write('we see how the function and slider works and options')


trees_df = pd.read_csv('trees.csv')
#setting the requriment columns 
column1,column2,column3 = st.columns(3)

with column1:
    st.header('column1')
    st.write('this is the sample text')
    st.image('https://imgs.search.brave.com/NYWbKEXuAKZbfSiHjR5WvbqnNDMwySUVD5WPOwvCR-o/rs:fit:1080:1200:1/g:ce/aHR0cHM6Ly9pbWFn/ZXMudW5zcGxhc2gu/Y29tL3Bob3RvLTE1/Mjk0Mjk2MTcxMjQt/OTViMTA5ZTg2YmI4/P2l4bGliPXJiLTAu/My41JnE9ODAmZm09/anBnJmNyb3A9ZW50/cm9weSZjcz10aW55/c3JnYiZ3PTEwODAm/Zml0PW1heCZpeGlk/PWV5SmhjSEJmYVdR/aU9qRXlNRGQ5JnM9/NGJlNmYyOWQwOTVi/YzU2Y2I4MDBjYzA4/ZWE2YjM0ODA')
with column2:
    st.header('column2')
    st.write('this is the sample text')
    st.image('https://imgs.search.brave.com/X58KK1O9d4q9jhmdPtuZlqyrN6JWmDb1is7HI0JEn98/rs:fit:600:900:1/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vNzM2/eC8yOC80OC85ZC8y/ODQ4OWRlMTMwMDIw/N2ViZTdlZmNiZmM3/NDU3NzAwOS5qcGc')
with column3:
    st.header('column3')
    st.write('this is the sample text')
    st.image('https://imgs.search.brave.com/qp9wgAVXsvRKVmvtLoxldjxwwjTJDuZBv6XngHABWK8/rs:fit:736:1107:1/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vNzM2/eC80Ny8yYi82MS80/NzJiNjFkNDliYjJj/ODQ3YmI3ZTA2NjU0/OTdhZjQ3ZS5qcGc')

column4,column5,column6 = st.columns(3)

with column4:
    st.header('data')
    st.write(trees_df['species'].head(10))
with column5:
    st.header('data')
    st.write(trees_df['address'].head(10))
with column6:
    st.header('data')
    st.write(trees_df['legal_status'])

