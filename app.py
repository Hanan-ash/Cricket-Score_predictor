import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('model.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Cape Town',
 'Auckland',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Nottingham',
 'Lauderhill',
 'Hamilton',
 'Manchester',
 'Abu Dhabi',
 'Centurion',
 'Southampton',
 'Mount Maunganui',
 'Mumbai',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Cardiff',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Christchurch',
 'Trinidad']

st.title('T20 Cricket Score Predictor')

col1, col2, col3 = st.columns(3)

with col1:
    batting_team = st.selectbox('Select Batting Team',sorted(teams))

with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))
if batting_team == bowling_team:
 st.error('Please Choose different teams')

with col3:
 city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score', min_value=0)
with col4:
    overs = st.number_input('Overs done(works for over>5)', min_value=5, max_value=19)
with col5:
    wickets = st.number_input('Wickets out', min_value=0,max_value=10)

last_five = st.number_input('Runs scored in last 5 overs', min_value=0)

if st.button('Predict Score'):
    balls_left = 120 -(overs*6)
    wickets_left = 10 - wickets
    crr = current_score/overs

    with st.spinner('In progress...'):
     input_df = pd.DataFrame(
      {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city, 'current_score': [current_score],
       'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})
     # st.table(input_df)
     result = pipe.predict(input_df)
     #st.header("Predicted Score - " + str(int(result[0])))
    st.success("Predicted Score - " + str(int(result[0])))


