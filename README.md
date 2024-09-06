# Anime Recommendation System

## Overview
The Anime Recommendation System is a web application built with Streamlit that helps users find anime similar to their favorite shows. It utilizes a recommendation algorithm based on Singular Value Decomposition (SVD) to suggest anime based on user-selected preferences.

## Hosted App
The Anime Recommendation System is hosted and accessible online at [Anime Recommendation Tools](https://animerecommendationtools.streamlit.app/). This hosted version allows you to:
- **Explore the Application:** Use the live interface to search for anime and receive recommendations.
- **Try it Out:** Experiment with different anime selections to see the recommendations in action.
  
## Features
- **Anime Search:** Allows users to select an anime from a list to find similar shows.
- **Recommendations:** Provides a list of recommended anime based on similarity.
- **Interactive Interface:** Built using Streamlit for a seamless user experience.

## Technologies Used
- **Python:** Programming language used for developing the application.
- **Streamlit:** Framework for building the web application.
- **Pandas:** Data manipulation and analysis library.
- **NumPy:** Numerical computing library.
- **Scikit-Learn:** Machine learning library used for SVD.
- **Requests:** Library for making HTTP requests to fetch anime details.
- **SciPy:** Library used for sparse matrix operations.

## Streamlit
**Streamlit** is an open-source framework designed to create web applications for data science and machine learning projects quickly and easily. It allows you to build interactive web applications with Python scripts. Streamlit is particularly well-suited for:
- **Rapid Development:** Quickly build and deploy applications without needing extensive web development knowledge.
- **Interactivity:** Easily create widgets like sliders, buttons, and text inputs to make your applications interactive.
- **Integration:** Seamlessly integrate with popular data science libraries such as Pandas, NumPy, and Scikit-Learn.
- **Live Code Updates:** Automatically updates the app whenever you modify the source code, providing immediate feedback during development.

In this project, Streamlit is used to build an interactive user interface where users can select anime, view recommendations, and explore anime details. Streamlit handles the rendering of the user interface and integrates with the backend logic for data processing and recommendation.

## Data Files
The application uses two CSV files:
1. **anime.csv**: Contains information about various anime shows, including their ID, name, genre, type, episodes, rating, and members. This file is essential for matching anime shows and filtering them based on user preferences.
2. **rating.csv**: Contains user ratings for the anime shows, including anime ID, user ID, and rating. This file is used to compute the similarity between different anime shows.

**Note:** The `anime.csv` and `ratings.csv` files are stored using Git Large File Storage (LFS) due to its large size. Git LFS helps manage large files efficiently and ensures that the repository remains lightweight.

## Algorithm
The recommendation algorithm uses Singular Value Decomposition (SVD) to identify and suggest anime shows similar to the one selected by the user. SVD is a matrix factorization technique that decomposes the user-item rating matrix into singular value matrices. This helps in capturing the underlying patterns and relationships between items, thereby providing accurate recommendations.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact
For any questions or feedback, you can reach me at: (yst1303@gmail.com)   
