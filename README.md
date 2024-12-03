# Movie Recommendation System with Regression

This is a Python-based movie recommendation system that provides movie suggestions based on user-selected categories. It also predicts IMDb ratings using a linear regression model.

## Features
- Display unique movie categories for user selection.
- Provide two options for movie recommendations:
  1. Top 10 movies with the highest IMDb ratings.
  2. 10 random movies from the selected category.
- Predict IMDb ratings for the selected category using a linear regression model.

## Technologies Used
- **Python**
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **scikit-learn**: For implementing linear regression.
- **Random**: For generating random samples.

## Prerequisites
1. Python 3.7+ installed on your system.
2. The following Python libraries installed:
   - `pandas`
   - `numpy`
   - `scikit-learn`
3. A CSV file containing the movie dataset:
   - The dataset must include at least the following columns:
     - `Movie Name`: Name of the movie.
     - `Category`: Category or genre of the movie.
     - `IMDB Rating`: IMDb rating of the movie.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
