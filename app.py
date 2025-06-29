from http.client import responses

import streamlit as st
import pickle
import pandas as pd
import requests
from huggingface_hub import hf_hub_download

API_KEY = st.secrets["OMDB_API_KEY"]

file_path = hf_hub_download(
    repo_id="MrSachin06/similarity",
    filename="similarity.pkl",
    repo_type="dataset"
)

st.set_page_config(page_title="Movie Recommender", layout="wide")

# Inject custom CSS for background and styling
st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem;
    }
    /* Background */
    body {
        background-image: url('https://img.freepik.com/free-photo/movie-background-collage_23-2149876028.jpg');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Overlay */
    .main {
        background-color: rgba(0, .5, 0, 0.75);
        padding: 2rem;
        border-radius: 10px;
        color: white;
    }

    /* Text Styling */
    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
    }

    /* Movie poster hover effect */
    img {
        border-radius: 10px;
        transition: transform 0.3s ease;
    }

    img:hover {
        transform: scale(1.05);
    }

    .stButton>button {
        color: white;
        background-color: #e50914;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }

    .stButton>button:hover {
        background-color: #b00610;
    }
    </style>
""", unsafe_allow_html=True)

def fetch_poster(movie,api):
    response = requests.get('https://www.omdbapi.com/?apikey={}>&t={}'.format(api,movie))
    data = response.json()
    
    if data.get('Response') == 'True' and data.get('Poster') != 'N/A':
            return data['Poster']
    else:
      return "https://thumbs.dreamstime.com/b/no-image-available-icon-177641087.jpg"

similarity = pickle.load(open(file_path,'rb'))
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:12]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].title,API_KEY))
    return recommended_movies, recommended_movies_posters




st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title('🎬 Movie Recommender System')
st.subheader('Created by Sachin')
st.write('Select a movie you like, and we’ll recommend similar ones!')

selected_movie_name = st.selectbox(
    '🔍 Search for your favorite movies',
    movies['title'].values
)

if st.button("Recommend"):
    with st.spinner("🔎 Finding similar movies..."):
        names, poster = recommend(selected_movie_name)
        st.markdown("### 🎥 Recommended Movies")

        for i in range(0, 12, 4):
            cols = st.columns(4)
            for j in range(4):
                if i + j < len(names):
                    with cols[j]:
                        st.image(poster[i + j], use_container_width=True)
                        st.caption(names[i + j])
st.markdown("</div>", unsafe_allow_html=True)


