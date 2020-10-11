from credentials import user_credentials
from user import Users


def create_user(username, email, password):
    """Function to create a new user"""
    new_user = Users(username, email, password)
    return new_user


def save_user(user):
    """Function to save user"""
    Users.save_users_details(user)


def delete_user(user):
    """Function to delete user"""
    user.delete_user()


def check_existing_users(username, password):
    """Function that check if user already exists"""
    verify_user = user_credentials.checking_user_details(username, password)
    return verify_user


def create_users_details(username, social_network, account_name, password):
    """Function to create user details"""
    new_user_details = user_credentials(
        username, social_network, account_name, password)
    return new_user_details


def save_users_details(details):
    """Function to save new user details"""
    user_credentials.save_user_details(details)


def display_user_details(username):
    """Function to display user details"""
    return user_credentials.display_user_details()


def automatic_generated_password():
    """Function for automatically generating passwords for users"""
    generated_password = user_credentials.automatic_generated_password()
    return generated_password


def main():

    while True:
        print(" ")
        print("WELCOME TO PYTHON PASSWORD-LOCKER")
        print(" ")
        print("""Select an option:
               1-Create an account
               2-Login to your account
               3-Exit Python Password Locker""")
        print(" ")
        option = int(input())

        if option == 1:
            print("Enter Username")
            username = input()
            print("________________________________________")

            print("Enter Emailaddress")
            email = input()
            print("_________________________________________")

            print("Enter New Password")
            password = input()
            save_user(create_user(username, email, password))
            print("__________________________________________")

            print(
                f"{username},you have successfully created an account, select login option")

        elif option == 2:
            print(" ")
            print("Please enter your details")
            print("___________________________________________")

            print("Enter Username")
            username = input()

            print("Enter Password")
            password = input()

            verifying_user = check_existing_users(username, password)
       
            if verifying_user == username:
                print(" ")
                print(f"{username}, welcome to python password locker")
                print(" ")
                while True:
                    print("___________________________________________")
                    print("""Select an option:
                            1-Add details to your account
                            2-Display your account details
                            3-End Session""")

                    option = int(input())

                    if option == 1:
                        print(" ")
                        print("Enter your details:")
                        print("____________________________________")

                        print("Which Social Media Network are you in..?")
                        social_network = input()
                        print("Account Name used in your choice above..")
                        account_name = input()
                        while True:
                           print(" ")
                           print("_______________________________________________")
                           print("""Select an option:
                            1-Use Own password
                            2-Use auto password generator
                            3-End Session""")
                           option = int(input())
                           print("_____________________________________________")
                           if option == 1:
                            print(" ")
                            print("Please Enter Your Password")
                            password = input()
                            break

                           elif option == 2:
                            password = automatic_generated_password()
                            break

                           elif option == 3:
                                break
                           else:
                            print("wrong option selected please try again!!")

                        save_users_details(create_users_details(username, social_network, account_name, password))
                        print(" ")
                        print(
                            "_________________________________________________________")
                        print("Details Created Successfully..!!")
                        print(
                            f"Social Media{social_network} \n Account Name: {account_name} \n Password: {password}")
                        print(" ")

                    elif option == 2:
                        print(" ")
                        if display_user_details(username):
                            print("List of your details")
                            print("____________________________________________")
                            for user_details in display_user_details(username):
                                print(
                                    f"Social Media: {user_details.social_network} \n Account Name: {user_details.account_name} \n Password: {user_details.password}")
                        else:
                         print(" ")
                         print("No user details to display")
                         print(" ")  
            else:
                print(" ")
                print("Wrong details entered..!!!")

        elif option == 3:
            break     
        else:
            print("________________________________________________")
            print(" ")
            print("wrong details entered...!!!")

if __name__ == '__main__':
    main()
