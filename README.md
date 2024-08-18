# **ANIME RECOMMENDATION SYSTEM**

This repository contains a collaborative filtering-based anime recommendation system implemented in Python. The project involves data processing, cleaning, and applying matrix factorization techniques to build a recommendation engine.

## **DATASET**

The project uses two datasets:

1. **ANIME DATASET**: Contains information about anime series and movies.
   - **`anime_id`**: Unique identifier for each anime
   - **`name`**: Title of the anime
   - **`genre`**: Genres of the anime
   - **`rating`**: Average rating of the anime
   - **`members`**: Number of members who have rated the anime

2. **RATING DATASET**: Contains user ratings for various anime.
   - **`user_id`**: Unique identifier for each user
   - **`anime_id`**: Identifier for the anime
   - **`rating`**: Rating given by the user

## **DATA PREPROCESSING**

- **CLEANING AND MERGING DATA**: Data from both datasets is merged based on **`anime_id`**. The merged data is cleaned by:
  - Removing HTML entities and unwanted characters from anime names
  - Handling missing values and duplicates
- **GENRE CONVERSION**: Genres are converted from a comma-separated string to a list for easier manipulation.

## **RECOMMENDATION SYSTEM**

1. **DATA AGGREGATION**:
   - Counts the number of ratings for each anime and filters out less popular anime based on a popularity threshold.

2. **PIVOT TABLE**:
   - Creates a user-item matrix where rows represent users, columns represent anime, and values represent ratings.

3. **MATRIX FACTORIZATION**:
   - Uses Truncated Singular Value Decomposition (SVD) to reduce dimensionality and identify patterns in user preferences.

4. **CORRELATION ANALYSIS**:
   - Computes the correlation matrix to find anime with similar ratings.

## **RESULTS**

The system identifies similar anime based on user ratings. For example, given an anime like **"Dragon Ball"**, the system recommends similar titles such as **"Bleach"**, **"Dragon Ball Z"**, **"Fullmetal Alchemist"**, and **"Naruto"**.

## **USAGE**

1. **RUN THE JUPYTER NOTEBOOK**: Execute the code in the Jupyter notebook to perform data preprocessing, build the recommendation system, and view the results.
