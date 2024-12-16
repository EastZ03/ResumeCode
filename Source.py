# This module contains the main menu for the program and the AdminAcc class to initialize the admins. 
# AdminAcc – creates the Admin class that holds their username and password
# Main() – calls on an instance of the Admin module, the Buyer module, and the Seller module to create a list of menu options for users
# Conditions are set in place to prevent a user from selecting options outside of the given menu choices
# Because the program requires sellers to input a book, and buyers to purchase books, the Admin must create an instance of a “seller” and a “buyer” in that order
import Buyer
import Admin


class AdminAcc:
    def __init__(self, name, email, passwd):
        self.__name = name
        self.__email = email
        self.__passwd = passwd

    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email
    
    def getPasswd(self):
        return self.__passwd

    def __str__(self):
        return( f'{self.__name}: your name| {self.__email}: your email|' 
               f'{self.__passwd}: your password| ')



def main():
    admin = Admin.AdminMod()
    while True:
        print("Main menu for the Knight's BookExchange")
        print("option (1): Admin Login")
        print("option (2): Login to Purchase")
        print("option (3): Login to Sell")
        print("Option (4): Exit")

        select = input("Please Select an Option Via Its Number:")
        print("\n")
        if select == '1': 
            admin.admin_function()
        elif select == '2':
            Buyer.buyer(admin)
        elif select == '3':
            import Seller
            Seller.seller(admin)
        elif select == '4':
            print("Thank you for using Knight BookExchange! Now closing this program...")
            break
        else:
            print("ERROR: This is not a valid option. Please select the number associated with the option.")
if __name__ == "__main__":
    main()