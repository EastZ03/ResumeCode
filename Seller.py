# To start, seller.py imports AdminMod from Admin to get the SellerList users, and BookInfo to
# interact with the entries that will be added to the BookList list
# Book_mod – creates an instance of BookInfo.BookMod
from Admin import AdminMod
import Buyer
import Source
import BookInfo
book_mod = BookInfo.BookMod()

# Seller – creates the main menu for the sellers; before a seller can interact with the menu,
# they must validate their name and username against the SellerList in the Admin module. If the
# credentials that are given match a corresponding name and username, then the user will be able
# to login; if the credentials do not match, they will be returned to the menu 
def seller(admin: AdminMod):
    
    print("Here you can log into an seller account")
    logename = input("Please supply your email address:")
    loguser = input("Please supply a username:")

    found_user = False
    for seller in admin.SellerList:
        if logename == seller.getEmail() and loguser == seller.getUsername():
            print(f"Welcome back {logename}")
            found_user = True
            
            print("What do we want to do today?")
            while True:
                print("\n")
                print("Option (1): List a Book")
                print("Option (2): Delete a Book")
                print("Option (3): View all Books in the Catalog")
                print("Option (4): Logout")
                response = input("Choose an Option:")

# Option1: Book_mod.get_book_from_user – book_mod is an instance of BookInfo.BookMod which calls on the
# get_book_from_user function in BookInfo.py to add a book to the BookList 
                if response == "1":
                    book_mod.get_book_from_user()

# Option2: Book_mod.remove_user_defined_book- book_mod is an instance of BookInfo.BookMod which calls on
# the remove_user_defined_book function in BookInfo.py to remove a book from the BookList 
                elif response == "2":
                    book_mod.remove_user_defined_book()

# Option3: Book_mod.displaybook- book_mod is an instance of BookInfo.BookMod which calls on the displaybook
# function in BookInfo.py to display all the books in the list 
                elif response == "3":
                    book_mod.displaybook()

# Option4: “Exit”- breaks from the Seller module and returns to Source.py
                elif response == "4":
                    print(f"Thank you for your business {logename}!")
                    break
                else:
                    print("Invalid Response...Please Retype")
    if not found_user:
        print("You did not supply valid information. Returning to menu...")
                   
