import pandas as pd 
import streamlit as st 
from math import radians , sin,cos,atan2,sqrt

airport_distance = pd.read_csv('https://raw.githubusercontent.com/tylerjrichards/Streamlit-for-Data-Science/main/job_application_example/airport_location.csv')


def haversine_distance(longitude1,latitude1,longitude2,latitude2,degree =False):

        if degree == True:
            longitude1 = radians(longitude1)
            latitude1 = radians(latitude1)
            longitude2 = radians(longitude2)
            latitude2 = radians(latitude2)

        a = sin((latitude2-latitude1)/2)**2 +cos(latitude1)*cos(latitude2)*sin((longitude2-longitude1)/2)**2
        c = 2*atan2(sqrt(a), sqrt(1-a))
        #converting radius into km
        distance =  6371 *c
        return(distance)
long1 = st.number_input('Longitude 1', value=2.550000) 
long2 = st.number_input('Longitude 2', value=172.531998)
lati1 = st.number_input('Latitude1', value=-43.489399)
lati2 = st.number_input('Latitude2' ,value=49.012798)

distance = haversine_distance(long1, lati1, long2, lati2,degree=True)

st.write('your dsitance is :{}km'.format(distance))




