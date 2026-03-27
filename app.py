import os
import requests
import pickle

FILE_URL = "https://drive.google.com/uc?id=1ck1WXQgNuksXbe-sA-ipP1QJ5JzeC1Zw"
FILE_NAME = "similarity.pkl"

def download_file():
    response = requests.get(FILE_URL, stream=True)
    with open(FILE_NAME, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

# Download only if not exists
if not os.path.exists(FILE_NAME):
    print("Downloading similarity.pkl...")
    download_file()
    print("Download complete!")

# Load file
similarity = pickle.load(open(FILE_NAME, "rb"))
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