#Joshua Williams

#start the program
if __name__ == "__main__":
    #loop while the user wants to continue
    while True:
        #display the menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        #get user input
        menu_choice = int(input("Please enter an option: "))
        #carry out the selected action
        if menu_choice == 1:
            password_choice = int(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif menu_choice == 2:
            pass

        elif menu_choice == 3:
            break
