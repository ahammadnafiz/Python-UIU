import os

file_name = 'movierating.txt'

def load_rating():
    ratings = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as data:
            for line in data:
                rating = eval(line.strip())
                ratings.append(rating)
    return ratings


def get_valid_input(prompt):
    while True:
        user = input(prompt).strip()
        if user:
            return user
        else:
          print('Please input a valid information')


def get_valid_rating(prompt):
    while True:
        try:
            movie_rating = float(input(prompt).strip())
            if 1 <= movie_rating <= 10:
                return movie_rating
            else:
                print('Rating should be between 1 and 10.')
        except ValueError:
            print('Invalid input. Please enter a numeric value for the rating.')


def save_data(ratings):
    with open(file_name, 'w') as data:
        for rating in ratings:
            data.write(f"{rating}\n")


def add_new_movie(ratings):
    movie_name = get_valid_input("Enter Your Movie Name: ")
    movie_rating = get_valid_rating("Enter Your Movie Rating: ")
            
    
    rating = {'movie_name': movie_name, 'movie_rating': movie_rating}
    ratings.append(rating)
    save_data(ratings)
    print('Movie rating added successfully!')
    

def view_all(ratings):
    print("Your Movie Rating Tracker")
    for index, rating in enumerate(ratings, start=1):
        print(f"{index}. Movie Name: {rating['movie_name']}, Movie Rating: {rating['movie_rating']}")
    print()


def update_movie_rating(ratings):
    view_all(ratings)  

    search_term = input("Enter the Movie name to update: ").strip().lower()
    
    update_rating = input('Enter New Rating: ').strip().lower()

    for movie in ratings:
        if search_term in movie['movie_name'].lower():
            movie['movie_rating'] = update_rating  # Update the key to 'movie_rating'
            save_data(ratings)  
            print(f"Rating for {movie['movie_name']} updated to {update_rating}")
            return

    print(f"Movie with name '{search_term}' not found in the list.")


def main():
    ratings = load_rating()
    
    while True:
        print("Choose an action:")
        print("1. View all movies and their ratings")
        print("2. Add a new movie along with a rating")
        print("3. Update an existing movie rating")
        print("4. Exit the program")
        
        user = input('Enter a choice: ')
        
        if user == '1':
            view_all(ratings)
        elif user == '2':
            add_new_movie(ratings)
        elif user == '3':
            update_movie_rating(ratings)
        elif user == '4':
            print('Good Bye')
            save_data(ratings)
            break
        else:
            print('Please Enter a valid action')

if __name__ == '__main__':
    main()
            