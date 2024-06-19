# Movie Recommender

A Python-based project that recommends 5 best movies related to a given movie using a dataset and machine learning techniques. The project uses the concept of vector similarity to find the best similar movies from the given movie and displays it on a streamlit based frontend application.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

This project leverages a dataset and machine learning algorithms to recommend movies. When a user inputs a movie, the system suggests 5 related movies based on various features.

## Features

- **Movie Recommendations:** Provides 5 best movie suggestions related to the input movie.
- **Data-Driven:** Uses a large dataset of movies for accurate recommendations.
- **Interactive Interface:** Simple and user-friendly interface to input and receive movie recommendations.

## Installation

To run this project locally:

1. Clone the repository:
    ```sh
    git clone https://github.com/Shreyansh203/Movie_recommender.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Movie_recommender
    ```
## Usage

1. Run the application:
    ```sh
    python main.py
    ```
2. Follow the on-screen prompts to input a movie and get recommendations.

## Folder Structure
```sh
    Movie_recommender/
├── .idea/
├── app.py
├── main.py
├── movie-checkpoint.ipynb
├── movie.ipynb
├── movies.pkl
├── movies_dict.pkl
├── tmdb_5000_movies.csv
```

- **.idea/**: Contains project-specific settings and configurations.
- **app.py**: Main application script.
- **main.py**: Script to run the recommendation system.
- **movie-checkpoint.ipynb**: Jupyter notebook checkpoint.
- **movie.ipynb**: Jupyter notebook for data analysis and model training.
- **movies.pkl**: Pickle file containing processed movie data.
- **movies_dict.pkl**: Pickle file containing movie dictionary.
- **tmdb_5000_movies.csv**: Dataset containing movie information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## Contact

For any inquiries or issues, please contact [Shreyansh](https://github.com/Shreyansh203).

