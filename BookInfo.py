# BookInfo.py does the work of adding books to Booklist. All of the work is only seen in the seller.py module.

import Source
import Admin

# Class Book- creates a new entity that consists of item number, book title, author, price, tag (with tag referencing whether the book is “available” or
# “sold”), and the company ID
class Book:
    def __init__(self, itemnum, title, author, price, tag, companyID):
        self.__itemnum = itemnum
        self.__title = title
        self.__author = author
        self.__price = float(price)
        self.__tag = tag
        self.__companyID = companyID
    
    def getItemnum(self):
        return self.__itemnum
    
    def getTitle(self):
        return self.__title
        
    def getAuthor(self):
        return self.__author
        
    def getPrice(self):
        return self.__price
    
    def getTag(self):
         return self.__tag
    
    def getCompanyID(self):
        return self.__companyID
    
    
    def __str__(self):
        return( f'{self.__itemnum}: Item Number|{self.__title}: book name| {self.__author}: author|' 
               f' {self.__price: .2f}: current price| {self.__tag}: seller tag| {self.__companyID} unique company identity')

# Class BookMod- initializes the BookList (global) for the book entries and hosts the other functions of the module
class BookMod:
    BookList = []

# Get_book_from_user- function that receives the input for a book name, author, item number, price, tag, and company ID.
#  An exception error will be raised if a value is not possible (i.e. the item number isn’t a number or the price is a
#  string). The argument received here is passed to try_add_book
    def get_book_from_user(self):
            response = input("Do you want to add a book to the store (Y/N)?")
            while response == "Y" or response == "y":
                try:
                    print("You may add books to the list here")
                    addname = input("Please give me the name of the book:")
                    addauthor = input("Give me the book author's name:")
                    additemnum = int(input("Give me the item number of the book:"))
                    addprice = float(input("How much is this book?"))
                    addtag = "available"
                    addcompID = input("Give me your company's unique ID:")
                except ValueError:
                    print("One of your values is not possible. Remember to use only numbers for the item number and a decimal style value (i.e. 14.95) for the book price.")
                if addtag != "sold" and addtag != "available":
                    print("You need to indicate the status of the book. Please Retry")
                else:
                    book = Book(additemnum, addname, addauthor, addprice, addtag, addcompID)
                    self.try_add_book(book)
                response = input("Do you want to add more books (Y/N)?")    

# Try_add_book- function that checks the Booklist by comparing the given item number to the item numbers in the list. If
# itemnum is not in the list, then the entry will be added to BookList. If itemnum is in the list, then the user will be
# given an error informing them that the item cannot be added 
    def try_add_book(self, book):
        if any(currentbook.getItemnum() == book.getItemnum() for currentbook in self.BookList):
            print("The item number is already associated with another book!")
        else:
            self.BookList.append(book)
            
# Remove_user_defined_book- function that receives the name of the book and the ID of the company that posted the book and
# passes it to try_remove_book 
    def remove_user_defined_book(self):
            response = input("Do we need to remove a book from the list (Y/N)?")
            if response.upper() == "Y":
                subname = input("Give me the exact name of the book:")
                id = input("Give me the company's id:")
                self.try_remove_book(subname, id)

# Try_remove_book- function that checks the BookList list to see if a book title and its corresponding ID exist. If it does exist,
# then the entry is removed; and if it does not exist, then an error is raised informing the user that the book does not exist
    def try_remove_book(self, title, companyID):
        for book in self.BookList:
            if book.getTitle() == title:
                if book.getCompanyID() == companyID:
                    self.BookList.remove(book)
                else:
                    print("ID not found")    
            else:
                print("Title not Found")

# Displaybook- prints the contents of BookList, or prints a message if no entries exist
    def displaybook(self):
        if not self.BookList:
            print("There is nothing to Display!")
        else:
            for item in self.BookList:
                print(item)
    