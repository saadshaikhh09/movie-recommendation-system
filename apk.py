import streamlit as st
import pickle
import numpy as np

# 🔥 CACHE LOADING (VERY IMPORTANT)
@st.cache_resource
def load_data():
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

movies_list = movies["title"].values


# 🔥 FAST RECOMMEND FUNCTION
def recommend(movie):
    try:
        movie_index = int(movies[movies["title"] == movie].index[0])
        distances = similarity[movie_index]

        # ⚡ FAST top 5 instead of full sort
        movie_indices = np.argsort(distances)[-6:-1]

        recommended_movies = []
        for i in movie_indices:
            recommended_movies.append(movies.iloc[i].title)

        return recommended_movies

    except Exception as e:
        st.error(f"Error: {e}")
        return []


# UI
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select The Movie",
    movies_list
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    for i in recommendations:
        st.write(i)