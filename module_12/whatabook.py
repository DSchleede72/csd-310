import mysql.connector
from mysql.connector import errorcode
import sys
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
db=mysql.connector.connect(**config)

#create method to show the main menu of WhatABook
def show_menu(): 
    print("\nMenu \n1. View Books \n2. View Store Locations \n3. My Account \n4. Exit Program ")
    try:
        choice = int(input("\n\nPlease enter the appropriate number character correlating with your requirement: "))
        return choice
    except ValueError:
        print("\n\nAn error has occurred. Please try running the program again.")
        sys.exit(0)

#create method to show all books belonging to WhatABook 
def show_books(cursor):
    #SELECT query 
    cursor.execute("SELECT book_name, author, book_id, details FROM book")
    books = cursor.fetchall()
    for book in books:
        print("\n\nBook Name: {} \nAuthor: {} \nBook ID: {}\nDetails: {}\n".format(book[0], book[1], book[2], book[3]))

#create method to show locations of all WhatABook stores
def show_locations(cursor):
    #SELECT query
    cursor.execute("SELECT locale, store_id FROM store")
    locations = cursor.fetchall()
    for location in locations:
        print("\n\nLocation: {}\nStore ID: {}".format(location[0], location[1]))

#create method to validate user ID
def validate_user():
    try:
        user_id = int(input("\n\nPlease enter your user ID using a character number: "))
        if user_id < 1 or user_id > 3:
            print("\n\nThe entered User ID is invalid. Please launch the program again.")
            sys.exit(0)
        
        return user_id
    except ValueError:
        print("\n\nAn error has occurred. Please launch the program again.")
        sys.exit(0)

#create method to show account options
def show_account_menu():
    print("\n\nCustomer Menu: \n1. View Wishlist \n2. Add Book to Wishlist \n3. Return to Main Menu")
    try:
        account_selection = int(input("\n\nWhat would you like to do with your account? "))
        if account_selection < 1 or account_selection > 3:
            print("\n\nThe entered account option is invalid.")
            
        return account_selection
    except ValueError:
        print("\n\nThe entered account option is invalid. Please launch the program again.")
        sys.exit(0)
        

#create method to show the user their wishlist
def show_wishlist():
     print("\n \nNow displaying the contents of your wishlist:")
     cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author, book.details FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
     wishlist = cursor.fetchall()

     for book in wishlist:
         print("\n\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[4], book[5], book[6]))

#create method to show which books the user can add to their wishlist
def available_for_wishlist():
    print("\n \nThe following books are available to add to your wishlist: ")
    cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id from wishlist WHERE user_id ={})".format(user_id))
    available = cursor.fetchall()
    for book in available:
        print("\n\nBook ID: {} \nBook Name: {} \n Author:{} \nDetails:{}".format(book[0], book[1], book[2], book[3]))

#create method to allow the user to add a book to their wishlist
def add_books():
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES ({}, {})".format(user_id, book_id))
    db.commit()
    cursor.execute("SELECT book_name, author from book where book_id = {}".format(book_id))
    added_book = cursor.fetchall()
    for book in added_book:
        print("\n\n'{}' by {} has been added to your wishlist!".format(book[0], book[1]))


try:
    cursor=db.cursor()
    print("\n\nThank you for choosing WhatABook!")
    user_select = show_menu()
    while user_select !=0:
        if user_select == 1:
            show_books(cursor)
            
        elif user_select == 2:
            show_locations(cursor)
        elif user_select ==3:
            user_id = validate_user()
            account_selection = show_account_menu()
            while account_selection > 0 and account_selection < 3:

                if account_selection ==1:
                    show_wishlist()
                if account_selection==2:
                 available_for_wishlist()
                 book_id = int(input("\n\nPlease enter the Book ID corresponding to the book you would like to add: "))
                 add_books()
                if account_selection < 0 or account_selection > 3:
                    print("\n\nAn invalid option was entered.")
                
                account_selection = show_account_menu()
        elif user_select ==4:
            print("\n\nProgram closed. Thank you for using WhatABook!")
            sys.exit(0)
        elif user_select < 1 or user_select > 4:
            print("\n\nAn invalid selection was entered. Please try again:")
        elif user_select != int:
            print("\n\nAn invalid selection was et")

        user_select = show_menu()              
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
