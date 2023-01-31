import streamlit as st
import pickle
import pandas as pd


def push_me_Hard(musics):
    music_index = music[music['Album'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_music = []
    for i in music_list:
        recommended_music.append(music.iloc[i[0]].Album)
    return recommended_music

music_dict = pickle.load(open('music_dict.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Music Recommender System')

slected_music_name = st.selectbox(
    'Hellooo  user, Choose any movie I will recommend you next fiveee ',
    music['Album'].values)

#button code
if st.button('Push me hard'):
    recomanditions = push_me_Hard(slected_music_name)
    for i in recomanditions:
        st.write(i)



