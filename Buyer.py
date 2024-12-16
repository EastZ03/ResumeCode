# Buyer.py imports AdminMod from Admin to perform a check against the buyer accounts in BuyerList (in the buyer function);
# and BookInfo.BookMod as the instance book_mod from the BookInfo module to obtain and modify the book entries
from Admin import AdminMod
import BookInfo
book_mod = BookInfo.BookMod()

# Option1: Purchase_book- function that receives an item number from the user and checks it against the BookList (an exception
# error will be raised if the input provided is not a number). If the item number has no corresponding book, then the user will
# be informed that no book exists with that number; if the book does exist, then book_purchased is called
def purchase_book():
    print("Here you may purchase a book from the system")
    response = input("Do you want to purchase a book (Y/N)?")
    if response.upper() == "Y":
        try:
            getnum = int(input("Give me the book's item number:"))
            for itemnum in book_mod.BookList:
                if getnum == itemnum.getItemnum():
                    print(f"The book that you want is '{itemnum.getTitle()}'")
                    confirm = input("Please confirm (Y/N):")
                    if confirm.upper() == "Y":
                        if itemnum.getTag() == "available":
                            book_purchased(itemnum)  
                        else:
                            print("This book is not available! Please try again")
                    break
                else:
                    print("There is no book available with that number!")            
        except ValueError:
            print("The value that you gave was not a valid integer")

# book_purchased- modifies the old book entry to change the tag to “sold” and re adds the item to the list, while also preventing the
# item from being sold once its tag changes; the user is then given a copy of their purchase as a receipt
def book_purchased(old_book):
    itemnum = old_book.getItemnum()
    title = old_book.getTitle()
    author = old_book.getAuthor()
    price = old_book.getPrice()
    tag = "sold"
    companyID = old_book.getCompanyID()
    new_book = BookInfo.Book(itemnum, title, author, price, tag, companyID)
    for changes, book in enumerate(book_mod.BookList):
        if book.getItemnum() == old_book.getItemnum():
            book_mod.BookList[changes] = new_book
            print(f"The book '{old_book.getTitle()}' has been sold.")
            print("\n")
            print("------------------------------------------")
            print("Receipt of purchase:")
            print("------------------------------------------")
            print(f'Item Number:{old_book.getItemnum()}')
            print(f'Book Name:{old_book.getTitle()}')
            print(f'Price paid:{old_book.getPrice()}')
            print("\n")
            print("Thank you for your purchase!. Press any key to contine")
            input()
            break 

def buyer(admin: AdminMod):
    
    print("Here you can log in to buy books!")
    logename = input("Please supply your email address:")
    loguser = input("Please supply a username:")

    found_user = False
    for buyer in admin.BuyerList:
        if logename == buyer.getEmail() and loguser == buyer.getUsername():
            print(f"Welcome back {logename}")
            found_user = True
            
            print("What do we want to do today?")
            while True:
                print("\n")
                print("Option (1): Purchase a Book")
                print("Option (2): View all Books in the Catalog")
                print("Option (3): Logout")
                response = input("Choose an Option:")

                if response == "1":
                    purchase_book()

# Option 2: displaybook- function that calls the BookList in BookMod.BookInfo to show all books in the library
                elif response == "2":
                    book_mod.displaybook()

# Option 3: exit- returns the user to the main menu
                elif response == "3":
                    print(f"Thank you for your business {logename}!")
                    break
                else:
                    print("Invalid Response...Please Retype")
    if not found_user:
        print("You did not supply valid information. Returning to menu...")
                
     