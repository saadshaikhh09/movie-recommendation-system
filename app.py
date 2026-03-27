import streamlit as st
import pickle
import requests

def recommend(movie):
    movie_index = int(movies[movies["title"] == movie].index[0])
    distances = similarity[movie_index]

    movies_list_sorted = [(i, float(j)) for i, j in sorted(
        enumerate(distances), key=lambda x: x[1], reverse=True
    )][1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for x in movies_list_sorted:
        movie_id = x[0]

        recommended_movies.append(movies.iloc[movie_id].title)

    return recommended_movies


movies = pickle.load(open("movies.pkl","rb"))   # ✅ dataframe
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = movies["title"].values   # ✅ only titles

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select The Movie",
    movies_list
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)