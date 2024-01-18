import streamlit as st
import pickle
import pandas as pd
import requests
import numpy as np


def poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=402efb6219c2f752fef2289f4345fa42&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/original' + data['poster_path']

def recemmend(movies):
    movie_index = movie[movie['title'] == movies].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),
                        reverse=True, key=lambda x: x[1])[1:6]

    recemmend_movie = []
    rec_movie_poster = []
    for i in movie_list:
        recemmend_movie.append(movie.iloc[i[0]].title)
        rec_movie_poster.append(poster(movie.iloc[i[0]].movie_id))  # Retrieve poster URL using the poster function
    return recemmend_movie, rec_movie_poster

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recemmndor System")

selected_movie_name = st.selectbox(
    "What Movie do you want to select", movie['title'].values)

if st.button('Recemmend Me'):
    names, posters = recemmend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
