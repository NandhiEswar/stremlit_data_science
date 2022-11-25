import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle


data = pd.read_csv('https://raw.githubusercontent.com/tylerjrichards/Streamlit-for-Data-Science/main/penguin_app/penguins.csv')
data.dropna(inplace=True)

output = data['species']

feature = data[['island','bill_length_mm','bill_depth_mm','flipper_length_mm', 'body_mass_g', 'sex']]

feature =pd.get_dummies(feature)

output, uniques = pd.factorize(output)

x_train, x_test, y_train, y_test = train_test_split(feature, output, test_size=.8)

rfc = RandomForestClassifier(random_state=15)

rfc.fit(x_train, y_train)

y_pred = rfc.predict(x_test)

score = accuracy_score(y_pred, y_test)

print('Our accuracy score for this model is {}'.format(score))
#pickle 
'''We now have two more files in our  folder, a file called random_forest_penguin.pickle, which contains our model, 
and output_penguin_.pickle, which has the mapping between penguin species and the output of our model. This is
it for the penguins_ml.py function! We can move on to our Streamlit app.'''
rf_pickle = open('random_forest_penguin.pickle', 'wb')
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open('output_penguin.pickle', 'wb')
pickle.dump(uniques, output_pickle)
output_pickle.close()

rf_pickle = open('random_forest_penguin.pickle', 'rb')

map_pickle = open('output_penguin.pickle', 'rb')

rfc = pickle.load(rf_pickle)

unique_penguin_mapping = pickle.load(map_pickle)

rf_pickle.close()

map_pickle.close()

island = st.selectbox('Penguin Island', options=['Biscoe', 'Dream', 'Torgerson'])

sex = st.selectbox('Sex', options=['Female', 'Male'])

bill_length = st.number_input('Bill Length (mm)', min_value=0)

bill_depth = st.number_input('Bill Depth (mm)', min_value=0)

flipper_length = st.number_input('Flipper Length (mm)', min_value=0)

body_mass = st.number_input('Body Mass (g)', min_value=0)

island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == 'Biscoe':
    island_biscoe = 1
elif island == 'Dream':
    island_dream = 1
elif island == 'Torgerson':
    island_torgerson = 1

sex_female, sex_male = 0, 0

if sex == 'Female':
    sex_female = 1
elif sex == 'Male':
    sex_male = 1

new_prediction = rfc.predict([[bill_length, bill_depth, flipper_length,body_mass, island_biscoe, island_dream,island_torgerson, sex_female, sex_male]])

prediction_species = unique_penguin_mapping[new_prediction][0]

st.write('We predict your penguin is of the {} species'.format(prediction_species))