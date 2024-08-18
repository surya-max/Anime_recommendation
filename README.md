Anime Recommendation System
This repository contains a collaborative filtering-based anime recommendation system implemented in Python. The project involves data processing, cleaning, and applying matrix factorization techniques to build a recommendation engine.

Dataset
The project uses two datasets:

Anime Dataset: Contains information about anime series and movies.

anime_id: Unique identifier for each anime
name: Title of the anime
genre: Genres of the anime
rating: Average rating of the anime
members: Number of members who have rated the anime
Rating Dataset: Contains user ratings for various anime.

user_id: Unique identifier for each user
anime_id: Identifier for the anime
rating: Rating given by the user
Data Preprocessing
Cleaning and Merging Data: Data from both datasets is merged based on anime_id. The merged data is cleaned by:
Removing HTML entities and unwanted characters from anime names
Handling missing values and duplicates
Genre Conversion: Genres are converted from a comma-separated string to a list for easier manipulation.
Recommendation System
Data Aggregation:

Counts the number of ratings for each anime and filters out less popular anime based on a popularity threshold.
Pivot Table:

Creates a user-item matrix where rows represent users, columns represent anime, and values represent ratings.
Matrix Factorization:

Uses Truncated Singular Value Decomposition (SVD) to reduce dimensionality and identify patterns in user preferences.
Correlation Analysis:

Computes the correlation matrix to find anime with similar ratings.
Results
The system identifies similar anime based on user ratings. For example, given an anime like "Dragon Ball", the system recommends similar titles such as "Bleach", "Dragon Ball Z", "Fullmetal Alchemist", and "Naruto".

Usage
Run the Jupyter Notebook: Execute the code in the Jupyter notebook to perform data preprocessing, build the recommendation system, and view the results.
Dependencies: Ensure you have the required Python libraries installed. You can install them using:
bash
Copy code
pip install pandas numpy matplotlib seaborn scikit-learn
Contributing
Feel free to open issues or submit pull requests to contribute to the project.
