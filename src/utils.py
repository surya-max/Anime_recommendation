import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
import requests
import streamlit as st

# Load data from CSV files
@st.cache_data
def load_data():
    try:
        anime = pd.read_csv('content/anime.csv')
        ratings = pd.read_csv('content/rating.csv')
        return anime, ratings
    except FileNotFoundError as e:
        st.error(f"Error loading data: {e}")
        return None, None

# Preprocess and filter data
@st.cache_data
def preprocess_and_filter_data(anime, ratings):
    df = pd.merge(ratings, anime, on="anime_id")
    df = df.drop(['genre', 'rating_y', 'members'], axis=1)
    
    # Clean 'name' column
    df['name'] = (df['name']
                  .str.replace('"', '', regex=False)
                  .str.replace(r'[^\w\s]', '', regex=True)
                  .str.strip()
                  .str.lower())
    
    # Count ratings
    rating_count = (df.groupby(by=['name'])['rating_x']
                    .count()
                    .reset_index()
                    .rename(columns={'rating_x': 'rating_count'})
                    [['name', 'rating_count']])
    
    rating_count['name'] = (rating_count['name']
                            .str.replace('"', '', regex=False)
                            .str.replace(r'[^\w\s]', '', regex=True)
                            .str.strip()
                            .str.lower())
    
    combined_rating_count = df.merge(rating_count, on='name', how='left')
    
    # Filter for popular ratings
    popularity_threshold = 4000  # Adjusted threshold
    popular_ratings = combined_rating_count.query('rating_count >= @popularity_threshold')
    popular_ratings = popular_ratings.drop_duplicates(['user_id', 'name'])
    
    pivottable = popular_ratings.pivot(index='user_id', columns='name', values='rating_x')
    pivottable = pivottable.fillna(0)
    
    return pivottable

# Compute SVD and correlation matrix
@st.cache_data
def compute_svd_and_corr(pivottable):
    X = csr_matrix(pivottable.values.T)
    SVD = TruncatedSVD(n_components=20, random_state=17)
    matrix = SVD.fit_transform(X)
    corr = np.corrcoef(matrix)
    return corr

# Fetch anime details from an API
@st.cache_data
def fetch_anime_details(anime_name):
    base_url = "https://api.jikan.moe/v4/anime"
    query = f"?q={anime_name}&limit=1"
    try:
        response = requests.get(base_url + query)
        response.raise_for_status()
        data = response.json()
        if data['data']:
            anime_info = data['data'][0]
            return {
                "title": anime_info.get('title', 'N/A'),
                "url": anime_info.get('url', '#'),
                "image_url": anime_info.get('images', {}).get('jpg', {}).get('image_url', ''),
                "synopsis": anime_info.get('synopsis', 'No synopsis available.')
            }
    except requests.RequestException as e:
        st.error(f"Error fetching anime details: {e}")
    return None

# Display anime details
def display_anime_details(anime_details):
    if anime_details:
        st.image(anime_details['image_url'], width=200)
        st.write(f"**[{anime_details['title']}]({anime_details['url']})**")
        st.write(anime_details['synopsis'])
    else:
        st.write("No information found.")

# Paginate recommendations
def paginate_recommendations(recommendations, page_size=5):
    total_pages = len(recommendations) // page_size + int(len(recommendations) % page_size > 0)
    
    # Initialize page_number in session_state if not present
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 0
    
    page_number = st.session_state.page_number

    # Display the current page of recommendations
    start_idx = page_number * page_size
    end_idx = start_idx + page_size
    for rec in recommendations[start_idx:end_idx]:
        rec_details = fetch_anime_details(rec)
        display_anime_details(rec_details)
    
    # Navigation buttons
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Previous", disabled=page_number == 0):
            st.session_state.page_number = max(st.session_state.page_number - 1, 0)
            # st.experimental_rerun()  

    with col2:
        if st.button("Next", disabled=page_number >= total_pages - 1):
            st.session_state.page_number = min(st.session_state.page_number + 1, total_pages - 1)
            # st.experimental_rerun()  
