#Joshua Williams

#Encode the password
def encode(password):
    new_password = ""
    for i in password:
        if (int(i) + 3) <= 9:
            new_password += str(int(i) + 3)
        else:
            new_password += str(int(i) - 7)
    return new_password

# Melissa Calixte
# decode the password
def decode(password):
    decoded_password = ""
    for i in password:
        i = int(i)
        if 1 <= i < 3:
            i = i + 7
        else:
            i = i - 3

        decoded_password += str(i)


    return decoded_password

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
            password = ""
            while len(password) != 8:
                password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            password = encode(password)
            print(password)
        elif menu_choice == 2:
            print(f'The encoded password is {password}. and the original password is {decode(password)}.')
            pass
        elif menu_choice == 3:
            break
        print()
