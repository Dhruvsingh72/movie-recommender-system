import pickle
import streamlit as st
import pandas as pd
import requests
import gdown
import os

# DOWNLOAD similarity.pkl FROM GOOGLE DRIVE
# -----------------------------
def download_similarity():
    file_id = "18LFMmUrvDL5NaPHIyhj52CidJrACNO4G"    # your file ID
    dest = "similarity1.pkl"
    
    if not os.path.exists(dest):
        print("Downloading similarity.pkl...")
        gdown.download(f"https://drive.google.com/uc?id={file_id}", dest, quiet=False)

download_similarity()   # call function before loading pickle


# Function to fetch poster 
def fetch_poster(movie_id):    #it will hit the api and for that we needed a library 'requests'
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a4c7924536578078767eba2154896fc6&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# function to recommend movies
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    sorted_movies_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in sorted_movies_list:
        movie_id = movies_list.iloc[i[0]].movie_id              # for the poster fetching from the tmbd api
        
        recommended_movies.append(movies_list.iloc[i[0]].title)

        #fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies ,recommended_movies_poster


# load dataset
movies_list = pickle.load(open('movies.pkl','rb'))

# load similarity variable
similarity= pickle.load(open('similarity1.pkl','rb'))

# Title name
st.title("Movie Recommender System")

# Select box with all the movies name - scroll
movies_title = movies_list['title'].values
Selected_movie_name = st.selectbox( "Choose Movie",(movies_title))

# There is a button recommend , when we click on any movie or type it comes in select box then click on recommend button it will call function
if st.button('Recommend'):
    names,posters = recommend(Selected_movie_name)
    
    col1, col2, col3, col4, col5= st.columns(5)   # updated from beta_columns to columns
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
