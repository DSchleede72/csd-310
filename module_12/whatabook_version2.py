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

#create a show books method
def show_books(cursor):
    #SELECT query 
    cursor.execute("SELECT book_name, author, book_id, details FROM book")
    books = cursor.fetchall()
    for book in books:
        print("\n\nBook Name: {} \nAuthor: {} \nBook ID: {}\nDetails: {}".format(book[0], book[1], book[2], book[3]))

#create method to show locations of all WhatABook stores
def show_locations(cursor):
    #SELECT query
    cursor.execute("SELECT locale, store_id FROM store")
    locations = cursor.fetchall()
    for location in locations:
        print("\n\nLocation: {}\nStore ID: {}".format(location[0], location[1]))

#create method to caputre and validate user ID
def validate_user(cursor):
    selected_id = (input("\n\nPlease enter your user ID: "))
    cursor.execute("SELECT user_id FROM user WHERE user_id = %s", (selected_id,))
    result = cursor.fetchone()
    if result:
            user_id = selected_id
            return user_id
            show_account_menu(user_id)
    else:
            print("An invalid user was selected. Please try again.")
            validate_user(cursor)

#create method to show user account options
def show_account_menu(user_id):
    print("\n\n-- Customer Menu -- \n1. View Wishlist \n2. Add Book to Wishlist \n3. Return to Main Menu")
    account_selection = input("\nWhat would you like to do with your account? ")
    if account_selection == ('1'):
        show_wishlist(user_id)
        show_account_menu(user_id)
    if account_selection == ('2'):
        available_for_wishlist(user_id)
        book_id = input("\nPlease enter the Book ID corresponding to the book you'd like to add to your wishlist: ")
        add_books(user_id, book_id)
        show_account_menu(user_id)
    if account_selection == ('3'):
        show_menu()
    if account_selection != ('1') or ('2') or ('3'):
        print("\nAn invalid account menu option was entered. Please try again.")
        show_account_menu(user_id)

#create method to show wishlist of selected user
def show_wishlist(user_id):
     print("\n \nNow displaying the contents of your wishlist:")
     cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author, book.details FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
     wishlist = cursor.fetchall()

     for book in wishlist:
         print("\n\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[4], book[5], book[6]))

#create available for wishlist method
def available_for_wishlist(user_id):
    print("\n \nThe following books are available to add to your wishlist: ")
    cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id from wishlist WHERE user_id ={})".format(user_id))
    available = cursor.fetchall()
    for book in available:
        print("\n\nBook ID: {} \nBook Name: {} \nAuthor:{} \nDetails:{}".format(book[0], book[1], book[2], book[3]))

#create method to add books to wishlist
def add_books(user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES ({}, {})".format(user_id, book_id))
    db.commit()
    cursor.execute("SELECT book_name, author from book where book_id = {}".format(book_id))
    added_book = cursor.fetchall()
    for book in added_book:
        print("\n\n'{}' by {} has been added to your wishlist!".format(book[0], book[1]))
    
#create method to show the main menu
def show_menu():
    print("\n\n\n-- Main Menu -- \n1. View Books \n2. View Store Locations \n3. My Account \n4. Exit Program ")
    user_select = (input('\n\nWhat would you like to do? '))
    if user_select == ('1'):
            show_books(cursor) 
            show_menu()   
    elif user_select == ('2'):
            show_locations(cursor)
            show_menu()
    elif user_select ==('3'):
           user_id = validate_user(cursor)
           account_selection = show_account_menu(user_id)
    elif user_select == ('4'):
        print("\nThe program will now be closed. Goodbye...!")
        sys.exit(0)
    elif '0' > user_select or user_select > '4':
         print("\n\nAn invalid option was entered. Please try again.")
         show_menu()
    
        
cursor=db.cursor()
print ("\n\nThank you for choosing WhatABook!")
show_menu()