import streamlit as st
import random
from src.utils import load_data, preprocess_and_filter_data, compute_svd_and_corr, fetch_anime_details, display_anime_details, paginate_recommendations

st.title("Anime Recommendation System")
st.subheader("Find anime similar to your favorite shows")

# Initialize progress bar
progress = st.progress(0)

# List of random questions
questions = [
    "What anime character do you identify with?",
    "What's your favorite anime genre?",
    "Which anime has the best opening song?",
    "Do you prefer subbed or dubbed anime?",
    "What was the first anime you ever watched?"
]

# Display a random question while loading
st.write(random.choice(questions))

try:
    # Step 1: Load data
    progress.progress(20)
    anime, ratings = load_data()
    if anime is None or ratings is None:
        st.error("Failed to load data. Please check the data files.")
        st.stop()

    # Step 2: Preprocess and filter data
    progress.progress(60)
    pivottable = preprocess_and_filter_data(anime, ratings)

    # Step 3: Compute SVD and correlation matrix
    progress.progress(90)
    corr = compute_svd_and_corr(pivottable)

    # Finalize progress
    progress.progress(100)
    st.write("Loading done! Thanks for hangin' out !!")

    # Anime selection
    anime_options = list(pivottable.columns)
    selected_anime = st.selectbox("Select an anime to find similar shows:", anime_options)

    if selected_anime:
        selected_anime = selected_anime.lower()  # Ensure it matches the case in pivottable
        if selected_anime in pivottable.columns:
            val1 = list(pivottable.columns).index(selected_anime)
            recommendations = list(pivottable.columns[(corr[val1] > 0.8) & (corr[val1] < 1)])  # Adjusted threshold

            # Fetch and display details of the selected anime
            st.write(f"**{selected_anime.title()} wiki:**")
            selected_anime_details = fetch_anime_details(selected_anime)
            display_anime_details(selected_anime_details)
            
            if recommendations:
                st.write(f"**Shows similar to {selected_anime.title()} are:**")
                paginate_recommendations(recommendations)  # Paginate the recommendations
            else:
                st.write(f"No similar shows found for {selected_anime.title()}. Try selecting a different anime.")
        else:
            st.write(f"{selected_anime.title()} not found in the database. Please select another anime.")
except Exception as e:
    st.error(f"An error occurred: {e}")
