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
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recomended_movies, recommended_movies_posters

movies_dict = pickle.load(open('D:\\amnil\\query\\movie-recommender-system\\movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict) 
similarity = pickle.load(open('D:\\amnil\\query\\movie-recommender-system\\similarity.pkl', 'rb'))


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How',
    movies['title'].values
)
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])