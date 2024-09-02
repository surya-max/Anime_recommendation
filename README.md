# Anime Recommendation System

## Overview

The Anime Recommendation System is a web application built with Streamlit that helps users find anime similar to their favorite shows. It utilizes a recommendation algorithm based on Singular Value Decomposition (SVD) to suggest anime based on user-selected preferences.

## Features

- **Anime Search**: Allows users to select an anime from a list to find similar shows.
- **Recommendations**: Provides a list of recommended anime based on similarity.
- **Interactive Interface**: Built using Streamlit for a seamless user experience.

## Technologies Used

- **Python**: Programming language used for developing the application.
- **Streamlit**: Framework for building the web application.
- **Pandas**: Data manipulation and analysis library.
- **NumPy**: Numerical computing library.
- **Scikit-Learn**: Machine learning library used for SVD.
- **Requests**: Library for making HTTP requests to fetch anime details.
- **SciPy**: Library used for sparse matrix operations.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Anime_recommendation.git
    cd Anime_recommendation
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run src/app.py
    ```

## Project Structure

- `src/`: Contains the source code for the application.
- `content/`: Contains the dataset files (`anime.csv` and `rating.csv`).
- `requirements.txt`: Lists the Python packages required for the project.
- `setup.py`: Script for setting up the package and dependencies.
- `README.md`: This file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.


## Contact

For any questions or feedback, you can reach me at: [yst1303@gmail.com](mailto:yst1303@gmail.com)

---

Happy anime watching and recommending!

