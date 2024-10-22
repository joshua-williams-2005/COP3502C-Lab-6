#Joshua Williams

#Encode the password
def encode(password):
    new_password = ""
    print(password)
    for i in password:
        if (int(i) + 3) <= 9:
            new_password += str(int(i) + 3)
        else:
            new_password += str(int(i) - 7)
    return new_password


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
            password_choice = ""
            while len(password_choice) != 8:
                password_choice = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = encode(password_choice)
        elif menu_choice == 2:
            pass

        elif menu_choice == 3:
            break
