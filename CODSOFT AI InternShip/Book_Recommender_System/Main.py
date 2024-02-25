
import pickle

# Define functions for recommendation systems
def popularity_based_recommendations():
    # Load data from pickle file
    popular_df = pickle.load(open('popular.pkl', 'rb'))

    # Display popular books
    print("Popular Books:")
    print(popular_df.head())


def collaborative_filtering_recommendations(book_title):
    # Load data from pickle file
    collaborative_df = pickle.load(open('popular.pkl', 'rb'))

    # Get recommendations based on the input book title
    recommendations = get_collaborative_filtering_recommendations(collaborative_df, book_title)

    # Display collaborative filtering recommendations
    print("Collaborative Filtering Recommendations for", book_title)
    print(recommendations.head())


# Function to get collaborative filtering recommendations based on input book title
def get_collaborative_filtering_recommendations(collaborative_df, book_title):
    # Your code to get recommendations based on the input book title
    # Example code:
    recommendations = collaborative_df[collaborative_df['Book-Title'] == book_title]
    return recommendations


# Main menu function
def main_menu():
    print("Welcome to the Recommendation System")
    print("1. Popularity Based Recommendations")
    print("2. Collaborative Filtering Recommendations")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        popularity_based_recommendations()
    elif choice == '2':
        book_title = input("Enter the book title you want recommendations for: ")
        collaborative_filtering_recommendations(book_title)
    elif choice == '3':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please enter a valid option.")

    # After executing the chosen recommendation system, return to the main menu
    main_menu()


# Start the main menu
main_menu()
