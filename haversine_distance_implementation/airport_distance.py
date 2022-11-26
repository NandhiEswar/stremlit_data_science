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
st.header('Enter the latitude and longitude ')        
long1 = st.number_input('Your Longitude ', value=2.550000) 
long2 = st.number_input('Destination Longitude ', value=172.531998)
lati1 = st.number_input('Your Latitude', value=-43.489399)
lati2 = st.number_input('Destination Latitude' ,value=49.012798)

distance = haversine_distance(long1, lati1, long2, lati2,degree=True)

st.write('your dsitance is :{}km'.format(distance))

def get_distance_list(airport_dataframe,airport_code):

    df = airport_dataframe.copy()

    row = df[df.loc[:,'Airport Code']== airport_code]
    lat = row['Lat']
    long = row['Long'] 
    df = df[df['Airport Code'] != airport_code]
    df['Distance'] = df.apply(lambda x: haversine_distance(latitude1=lat, longitude1=long,latitude2 = x.Lat, longitude2 = x.Long, degree=True),axis=1)
    return(df.sort_values(by='Distance').reset_index()['Airport Code'])

#airport_distance_df


selected_airport = st.selectbox('Airport Code', airport_distance['Airport Code'])
distance_airports = get_distance_list(airport_dataframe=airport_distance, airport_code=selected_airport)
st.write('Your closest airports in order are {}'.format(list(distance_airports)))
