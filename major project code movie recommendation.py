import pandas as pd
import random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Load the dataset with the correct encoding
file_path = "C:\\Users\\admin\\OneDrive\\Desktop\\python2\\movie_dataset(1).csv"
try:
    df = pd.read_csv(file_path, encoding='latin1')  # Use 'latin1' or other encoding if utf-8 fails
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")
    exit()

# Add a dummy feature for linear regression (numerical encoding of categories)
df['Category_Encoded'] = df['Category'].astype('category').cat.codes

# Prepare the data for regression
X = df[['Category_Encoded']]  # Independent variable(s)
y = df['IMDB Rating']  # Dependent variable

# Split data into training and testing sets for regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Define the updated movie recommendation program
def movie_recommendation_with_regression():
    try:
        # Display all unique categories
        print("Available Categories:")
        categories = df['Category'].unique()
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category}")

        # User selects a category
        try:
            category_choice = int(input("Select a category by entering its number: "))
            if category_choice < 1 or category_choice > len(categories):
                raise ValueError("Invalid category number.")
            selected_category = categories[category_choice - 1]
            print(f"You selected: {selected_category}\n")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid category number.")
            return

        # Filter movies based on selected category
        filtered_movies = df[df['Category'] == selected_category]

        # Offer two options to the user
        print("Choose an option:")
        print("1. Get 10 movies with the highest IMDb ratings")
        print("2. Get 10 random movies")

        try:
            option = int(input("Enter your choice (1 or 2): "))
            if option not in [1, 2]:
                raise ValueError("Invalid option selected.")

            if option == 1:
                # Display top 10 movies by IMDb rating
                top_movies = filtered_movies.sort_values(by='IMDB Rating', ascending=False).head(10)
                print("\nTop 10 movies by IMDb rating:")
                print(top_movies[['Movie Name', 'IMDB Rating']])
            elif option == 2:
                # Display 10 random movies
                random_movies = filtered_movies.sample(n=min(10, len(filtered_movies)))
                print("\n10 Random movies:")
                print(random_movies[['Movie Name', 'IMDB Rating']])

            # Predict IMDb ratings for the selected category using linear regression
            print("\nLinear Regression Prediction:")
            category_code = df[df['Category'] == selected_category]['Category_Encoded'].iloc[0]
            predicted_rating = regressor.predict(np.array([[category_code]]))
            print(f"Predicted IMDb rating for the category '{selected_category}': {predicted_rating[0]:.2f}")

        except ValueError as e:
            print(f"Error: {e}. Please enter a valid option.")
        except Exception as e:
            print(f"Unexpected error: {e}.")
    except Exception as e:
        print(f"An error occurred: {e}.")

# Run the updated program
movie_recommendation_with_regression()
print("\n\n****************************************************")
print("\nCREDITS FOR THE PROJECT \n1.Priyanshu TRIPATHI  TASK->CODING AND UPLOADING\n2.Tushar kumar  Task-> preparing hardcopy and preparing excel sheet\n3.Madhukant Task-> Preparing excel sheet and converting it in csv file")
