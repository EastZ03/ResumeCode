# To begin, the module imports BookInfo.py so that the instance of the BookList created in that module may be accessed in
# Admin.py under “Option 4: View All Books.”

import Source
import BookInfo
book_mod = BookInfo.BookMod()

# Class BuyerAcc—used to create the Buyer accounts that consists of a name, email, username, and role. Role is automatically
# assigned as “Buyer” because the user would be adding a buyer account
class BuyerAcc:
    def __init__(self, name, email, username, role):
        self.__name = name
        self.__email = email
        self.__username = username
        self.__role = role

    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email
    
    def getUsername(self):
        return self.__username
    
    def getRole(self):
        return self.__role
    
    def __str__(self):
        return( f'{self.__name} is your name| {self.__email}: is your email address|' 
               f'{self.__username} is your username| and {self.__role} is your position')            
    
# Class SellerAcc – inherits all of the attributes created in the Buyer class, while also adding compname as the company name for
# the Seller. The Role attribute here is assigned as “Seller” because the user would have requested to create a seller account
class SellerAcc(BuyerAcc):
    def __init__(self, name, email, username, role, compname):
        super().__init__(name, email, username, role)
        self.__compname = compname

    def getCompname(self):
        return self.__compname   

    def __str__(self):
        user_info = super().__str__()
        return( f'{user_info} | {self.__compname} is your company name|' )

class AdminAcc(BuyerAcc):
    def __init__(self, name, email, passwd):
        super().__init__(name, email)
        self.__passwd = passwd
    
    def getPasswd(self):
        return self.__passwd

    def __str__(self):
        user_info = super().__str__()
        return( f'{user_info} | {self.__passwd}: your password| ')

# Class AdminMod – used to initialize the BuyerList list (global) that holds all the entries of Buyer accounts; initialize the
# SellerList list (global) that holds all the entries of Seller Accounts; and hold all of the functions in the module
class AdminMod:

# Def __init__- initializes the class and holds the BuyerList and SellerList lists
    def __init__(self):
        self.BuyerList = []
        self.SellerList = []

# Option1: Def get_user_type – used to obtain what type of account that the user would like to create; Option 1 calls on get_buyer
# to add a buyer account, and Option 2 calls on get_seller to create a seller account
    def get_user_type(self):
            response = input("Do you want to create a new user (Y/N)?")
            if response == "Y" or response == "y":
                print("What type of user are you trying to add?")
                print("Option (1): Buyer")
                print("Option (2): Seller")
                choice = input("")

                if choice == "1":
                    self.get_buyer()
                elif choice == "2":
                    self.get_seller()

# Get_buyer – receives an input for the four attributes of the buyer (name, email, username, and role) and passes this information to try_add_buyer
    def get_buyer(self):
        response = input("Do you want to create a new user (Y/N)?")
        while response == "Y" or response == "y":
            print("You may create a new buyer account here!")
            addname = input("Please give me the name of the buyer:")
            addemail = input("Give me the buyer's email address. Do not include @gmail.com:")
            addusername = input("Give me a username for this person:")
            addrole = "buyer"
            buyeracc = BuyerAcc(addname, addemail + "@gmail.com", addusername, addrole)
            if "@" in addemail:
                print("Error: Do not include the domain name in your email.")
            elif addname == "" or addemail == "" or addusername == "" or addrole == "":
                print("The fields may not be left blank")
            else:
                self.try_add_buyer(buyeracc)
            response = input("Do you want to add more buyers (Y/N)?")         

# Try_add_buyer – obtains the information provided from get_buyer and performs a check against the BuyerList; if the email that was
# input into addemail is not in that list, then the user will be added to the BuyerList; if that email is in the list, then an error
# will appear and inform the user that the email already exists              
    def try_add_buyer(self, buyeracc):
        if any(currentuser.getEmail() == buyeracc.getEmail() for currentuser in self.BuyerList):
            print("The buyer is already in the list!")
        else:
            self.BuyerList.append(buyeracc)

# Get_seller- performs the same function as the get_buyer function, but instead passes the user input into the try_add_seller function     
    def get_seller(self):
        response = input("Do you want to create a new user (Y/N)?")
        while response == "Y" or response == "y":
            print("You may create a new seller account here!")
            addname = input("Please give me the name of the person selling:")
            addemail = input("Give me the seller's email address. Do not include @gmail.com:")
            addusername = input("Give me a username for this person:")
            addrole = "seller"
            addcompname = input("Give me your company's name:")
            selleracc = SellerAcc(addname, addemail + "@gmail.com", addusername, addrole, addcompname)
            if "@" in addemail:
                print("Error: Do not include the domain name in your email.")
            elif addname == "" or addemail == "" or addusername == "" or addrole == "" or addcompname == "":
                print("The fields may not be left blank")    
            else:
                self.try_add_seller(selleracc)
            response = input("Do you want to add more sellers (Y/N)?")

# Try_add_seller- checks the SellerList to see if the requested account is in that list. If there is not a matching email in that
# dictionary, then the user will be added; if that email already exists, then the user will receive an error that tells them
# the account already exists               
    def try_add_seller(self, selleracc):
        if any(currentuser.getEmail() == selleracc.getEmail() for currentuser in self.SellerList):
            print("The seller is already in the list!")
        else:
            self.SellerList.append(selleracc)

# Option2: Select_user_type_remove- used to allow users to make a choice of what type of user they would like to remove: Option 1
# calls the “remove_buyer” function and Option 2 calls the “remove_seller” function    
    def select_user_type_remove(self):
            response = input("Do we need to remove a user (Y/N)?")
            if response.upper() == "Y":
                print("Option (1): Buyer")
                print("Option (2): Seller")
                select = input("Give the number of the corresponding user:")
                if select == "1":
                    self.remove_buyer()
                elif select == "2":
                    self.remove_seller()
                else:
                    print("This is not a valid option. Returning to menu...")

# Remove_seller – receives an input for the seller’s full name and their email address and passes this information to try_remove_seller
    def remove_seller(self):
            response = input("Do we need to remove a seller (Y/N)?")
            if response.upper() == "Y":
                sellername = input("Give me the exact name of the seller:")
                selleremail = input("Give me the seller's full email address:")
                self.try_remove_seller(sellername, selleremail)

# Try_remove_seller- takes the input from remove_seller and checks it against the names and their corresponding emails in the SellerList;
# if the entry is in the list, then the item will be removed, and if the entry is not in the list, then the user will be given an error that
# informs them that the entry does not exist    
    def try_remove_seller(self, name, email):
        for item in self.SellerList:
            if item.getName() == name and item.getEmail() == email:
                self.SellerList.remove(item)
                print("Account successfully removed")
            else:
                print("There is no seller corresponding to that info")

# Remove_buyer – receives an input for the buyer’s full name and their email address and passes this information to try_remove_buyer
    def remove_buyer(self):
            response = input("Do we need to remove a buyer (Y/N)?")
            if response.upper() == "Y":
                buyername = input("Give me the exact name of the buyer:")
                buyeremail = input("Give me the seller's email address:")
                self.try_remove_buyer(buyername, buyeremail)           

# Try_remove_buyer- takes the input from remove_buyer and checks it against the names and their corresponding emails in the BuyerList;
# if the entry is in the list, then the item will be removed, and if the entry is not in the list, then the user will be given an error
# that informs them that the entry does not exist
    def try_remove_buyer(self, name, email):
        for item in self.BuyerList:
            if item.getName() == name and item.getEmail() == email:
                self.BuyerList.remove(item)
                print("Account Successfully Removed!")
            else:
                print("There is no buyer corresponding to that info")         

# Option3: Display_users- calls on the instances of both BuyerList and SellerList prints both for the user 
    def display_users(self):
        print("The entire list of buyers and sellers is printed here")
        print("\n")
        print("Here are the buyers")
        for item in self.BuyerList:
            print(item)
        print("\n")
        print("Here are the sellers")    
        for item in self.SellerList:
            print(item)

    def admin_function(self):
        admin_list = ["example@gmail.com"]
        pass_list = ["password"]
        
        print("Here you can log into an admin account")
        logname = input("Please supply your email address (for demo, example@gmail.com):")
        logpass = input("Please supply a password (for demo, password):")

        if logname in admin_list and logpass in pass_list:
            print(f"Welcome back {logname}")

            print("What do we want to do today?")
            while True:
                print("\n")
                print("Option (1): Create Buyer and Seller Account")
                print("Option (2): Delete Buyer and Seller Account")
                print("Option (3): View all users")
                print("Option (4): View all books")
                print("Option (5): Exit to Menu")
                response = input("Choose an Option:")

                if response == "1":
                    self.get_user_type()

                elif response == "2":
                    self.select_user_type_remove()

                elif response == "3":
                    self.display_users()

# Option4: Book_mod.displaybook- this function is different from the others listed above because it calls on an instance of BookList created in BookInfo.BookMod to display all the books in the library
                elif response == "4":
                    book_mod.displaybook()

# Option 5 will exit the Admin menu and return the user to the bookstore menu
                elif response == "5":
                    print(f"Thank you for your work {logname}!")
                    break