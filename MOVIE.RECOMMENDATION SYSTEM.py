import pandas as pd
import random

def show_movies(option):
    try:
        # File path
        file_path = "C:\\Users\\admin\\OneDrive\\Desktop\\python2\\MOVIES_NAME.xlsx_ALL_TYPE(1).second.csv"

        # Load the CSV file
        movies_df = pd.read_csv(file_path, encoding='ISO-8859-1', skiprows=2)
        
        # Rename columns
        movies_df.columns = ['Index', 'Thriller', 'Empty1', 'Action', 'Empty2', 'Romantic', 'Empty3', 'Comedy', 'Empty4', 'Horror']
        movies_df = movies_df.drop(columns=['Index', 'Empty1', 'Empty2', 'Empty3', 'Empty4'])
        
        # Strip whitespace from column names
        movies_df.columns = movies_df.columns.str.strip()

        # Category mapping
        categories = ['Thriller', 'Action', 'Romantic', 'Comedy', 'Horror']

        # Validate user input for category selection
        if option.isdigit():
            option = int(option)
            if 1 <= option <= len(categories):
                category = categories[option - 1]
            else:
                print("\nInvalid number. Please select a number between 1 and 5.")
                return
        else:
            print("\nInvalid input. Please enter a number between 1 and 5.")
            return

        # Check if the category exists in the DataFrame
        if category in movies_df.columns:
            movies_list = movies_df[category].dropna().tolist()

            # Ask the user to choose a display method
            print(f"\nYou selected the '{category}' category. How would you like to view the movies?")
            print("1. Random list of all movies")
            print("2. Top 10 movies by IMDb ratings (sorted)")

            view_choice = input("\nEnter your choice (1 or 2): ").strip()

            if view_choice == "1":
                # Display all movies in random order
                random.shuffle(movies_list)
                print("\n" + "="*30)
                print("            Metflix")
                print("="*30)
                print(f"\nMovies in the '{category}' category (random order):")
                for movie in movies_list:
                    print(f"- {movie}")
            elif view_choice == "2":
                # Display top 10 movies (using head())
                print("\n" + "="*30)
                print("            Metflix")
                print("="*30)
                print(f"\nTop 10 movies in the '{category}' category (IMDb ratings):")
                for movie in movies_list[:10]:
                    print(f"- {movie}")
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
        else:
            print("\nInvalid category. Please choose from:", ', '.join(categories))

    except FileNotFoundError:
        print("Error: The file could not be found. Please ensure the file path is correct.")
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file. Ensure it is a valid CSV format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Display menu and prompt user for input
print("\n                                            Welcome to Metflix!")
print("\n\nPlease select a category by entering the corresponding number:")
print("1. Thriller")
print("2. Action")
print("3. Romantic")
print("4. Comedy")
print("5. Horror")

option = input("\nWrite your choice: ").strip()
show_movies(option)
print("\n\n\nspecial credits of the project\n1.PRIYANSHU TRIPATHI\n2.MADHUKANT\n3.TUSHAR KUMAR ")