import streamlit as st 
import pickle 
import pandas as pd 
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recomended_movies = [] 
    recommended_movies_posters = []
    for i in movies_list:
        movie_id= movies.iloc[i[0]].movie_id
        recomended_movies.append(movies.iloc[i[0]].title)
    