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
print(users_dict)
#register_user(users_dict, " ", " ") # call the function
### user login
def login_user(users_dict):
    """login an existing user"""

    print("\n"
 "--- User Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username in users_dict and users_dict[username] == password: # check if username and password match #in is used to check if key exist in dictionary
        print(f"Welcome {username.capitalize()}") #capitalize first letter
        return username
    else:
        print("Invalid username or password!")
        return None
    
#login_user(users_dict) # call the function

###main menu function
def main_menu():
    """display main menu options"""

    print("="*55)
    print("∖n " \
    "--- Library Management System ---")
    print("="*55)
    print("1. Add Book")
    print("2. View Book")
    print("3. Search Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Logout")
    print("="*55)

#main_menu() # call the function

### add book function
def add_book(books_list, book_ids):
    """add a new book to the library"""

    print("\n"
 "--- Add New Book ---")
    book_id = input("Enter Book ID: ").strip()
    if book_id in book_ids:
        print("Book ID already exists!")
        return 
    
    title = input("Enter Book Title: ").strip()
    author = input("Enter Book Author: ").strip()
    quantity = int(input("Enter Quantity: ").strip())

    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'quantity': quantity
    }

    books_list.append(new_book)
    book_ids.add(book_id)

    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},{quantity}\n")

    print("Book added successfully!")

#books_list = load_books()
#book_ids = get_existing_books_ids(books_list)
#print(books_list)
#print(book_ids)
#add_book(books_list, book_ids) # call the function
  

### function to view all books in the library
def view_books(books_list):
    """view all books in the library"""

    print("\n"
 "--- All Books in the Library ---")
    if not books_list:
        print("No book found in the library!")
        return

    for book in books_list:
        print(f"{book['id']} | {book['title']} | {book['author']} | {book['quantity']}")
#view_books(books_list) # call the function

### search a book using title or author
def search_books(books_list):
    """search books by title or author"""
    def search_books(books_list):
        found_items = []
        search_term = input("Enter book title or author to search: ").strip().lower()
        for book in books_list:
            if search_term in book['title'].lower() or search_term in book['author'].lower():
                found_items.append(book)
        if found_items:
            print(f"found {len(found_items)} book(s):")
            view_books(found_items)
        else:
            print("No books found matching the search criteria.")
#search_books(books_list) # call the function

## save books to file
#write all books back to books.txt
def save_books(books_list):
    """save all books to books.txt file"""

    with open("books.txt", "w") as f: #w mode to overwrite the file/clear the file/update the file
        for book in books_list:
            f.write(f"{book['id']},{book['title']},{book['author']},{book['quantity']}\n")

            ##issue book > user can borrow a book if available(user le book lanu)
def issue_book(books_list):
    """issue a book to a user"""

    print("\n"
 "--- Issue Book ---")
    book_id = input("Enter Book ID to issue: ").strip()

    for book in books_list:
        if book['id'] == book_id:
            if book['quantity'] > 0:
                book['quantity'] -= 1
                save_books(books_list) # update the books.txt file
                print(f"Book '{book['title']}' issued successfully!")
                print(f"Remaining quantity: {book['quantity']}")
                return
            
            else:
                print("Sorry, this book is currently unavailable!")
                return

    print("Book ID not found!")

def return_book(books_list):
    """return a book to the library"""

    print("\n"
 "--- Return Book ---")
    book_id = input("Enter Book ID to return: ").strip()

    for book in books_list:
        if book['id'] == book_id:
            book['quantity'] += 1
            save_books(books_list) # update the books.txt file
            print(f"Book '{book['title']}' returned successfully!")
            print(f"Updated quantity: {book['quantity']}")
            return

    print("Book ID not found!")
#issue_book(books_list) # call the function
#return_book(books_list) # call the function

### main function -----> control flow of the program

def main():
    '''Main program loop'''
    users_dict = load_users()
    print("="*50)
    print(" Welcome to the Library Management System ")
    print("="*50)
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            register_user(users_dict)
        elif choice == '2':
            username = login_user(users_dict)
            if username:
                books_list = load_books()
                book_ids = get_existing_books_ids(books_list)
                while True:
                    main_menu()
                    user_choice = input("Enter your choice: ").strip()
                    if user_choice == '1':
                        add_book(books_list, book_ids)
                    elif user_choice == '2':
                        view_books(books_list)
                    elif user_choice == '3':
                        search_books(books_list)
                    elif user_choice == '4':
                        issue_book(books_list)
                    elif user_choice == '5':
                        return_book(books_list)
                    elif user_choice == '6':
                        print("Exiting the system. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main() 



        







    
    

       
      
