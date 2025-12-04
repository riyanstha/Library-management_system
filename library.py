"""
library management system
(register, login) > users
(add book, issue book, view book, search book, return book) > books
"""

### creating two file named users.txt and books.txt to store user information 
# and book information permanently inside the file

import os

if not os.path.exists("users.txt"): # checking if file exist
    with open("users.txt", "w") as f: # creating file
        pass

if not os.path.exists("books.txt"): # checking if file exist
    with open("books.txt", "w") as f: # creating file
        pass

###load data from the file
def load_users():
    """load all the users from users.txt into a dictionary"""

    user_dict = {}

    try:
        with open("users.txt", "r") as f:
            for line in f:
                line = line.strip() # remove any leading/trailing whitespace
                if line:
                    username, password = line.split(",") # split by comma
                    user_dict[username] = password

    except FileNotFoundError:
       print(" File not found!")

    return user_dict

def load_books():
    books_list = []

    try:
        with open("books.txt", "r") as f:
            for line in f:
                line = line.strip() # remove any leading/trailing whitespace
                if line:
                    book_id, title, author, quantity = line.split(",")

                    book = {
                        'id': book_id,
                        'title': title,
                        'author': author,
                        'quantity': int(quantity)
                    }
                    books_list.append(book)

    except FileNotFoundError:
       print(" File not found!")

    return books_list

def get_existing_books_ids(books_list):
   #create a set to store existing book IDs
   book_ids = set()

   for book in books_list:
       # dictonary
       book_ids.add(book['id'])

   return book_ids

### user registration
def register_user(user_dict, username, password):
    """register a new user"""

    print("∖n"
 "--- User Registration ---")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    if username in user_dict:
        print(f"Username already exists!")
        return False
    if not username or not password:
        print("Username and password cannot be empty!")
        return False
    user_dict[username] = password

    #save the registered user to the file "users.txt"
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Registration successful!")
    return True
users_dict = load_users()
register_user(users_dict , "", "")
    

       
      
