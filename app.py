import pandas as pd
import streamlit as st
import pickle
import requests
st.set_page_config(
    page_title="Your App Title",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded"
    #bgcolor="blue",  # You can use any valid CSS color here
)
st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    L=[]
    poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        L.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movie_id))
    return L,poster

movie_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
option=st.selectbox('Select a movie',movies['title'].values)

if st.button('Recommend'):
    recommended_movie_names, corresponding_posters = recommend(option)

    # Displaying movie name and poster in 6 columns
    column_1, column_2, column_3, column_4, column_5, column_6 = st.columns(6)
    with column_1:
        st.text(recommended_movie_names[0])
        st.image(corresponding_posters[0])

    with column_2:
        st.text(recommended_movie_names[1])
        st.image(corresponding_posters[1])

    with column_3:
        st.text(recommended_movie_names[2])
        st.image(corresponding_posters[2])

    with column_4:
        st.text(recommended_movie_names[3])
        st.image(corresponding_posters[3])

    with column_5:
        st.text(recommended_movie_names[4])
        st.image(corresponding_posters[4])

