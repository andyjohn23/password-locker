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
    return user_credentials.display_user_details(username)


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
               1. 1-Create an account
               2. 2-Login to your account
               3. 3-Exit Python Password Locker""")
        print(" ")
        option = int(input())

        if option == "1":
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

            print(f"{username},you have successfully created an account, select login option")

        elif option == "2":
            print(" ")
            print("Please enter your details")
            print("___________________________________________")

            print("Enter Emailaddress")
            email = input()

            print("Enter Password")
            password = input()
            verifying_user = check_existing_users(username, password)

            if verifying_user == username:
                print(" ")
                print(f"{username}, welcome to python password locker")
                print(" ")


if __name__ == '__main__':
    main()
