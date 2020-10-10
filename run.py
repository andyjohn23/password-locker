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

def check_existing_users(username,password):
    """Function that check if user already exists"""
    verify_user = user_credentials.checking_user_details(username, password)
    return verify_user


def main():

    while True:
        print(" ")
        print("WELCOME TO PYTHON PASSWORD-LOCKER")
        print(" ")
        print("""Select an option:
               1. "1"-Create an account(using own password)
               2. "2"-Login to your account
               3. "3"-Exit Python Password Locker""")
        print(" ")
        option = int(input())

        if option == "1":
            print("Enter Username")
            username = input()

            print("Enter Emailaddress")
            email = input()

            print("Enter New Password")
            password = input()
            print(" ")

            print(
                f"{username},you have successfully created an account, select login option")

        elif option == "2":
            print("Enter Emailaddress")
            email = input()

            print("Enter Password")
            password = input()

            print(
                f"{username}, welcome to python password locker")


if __name__ == '__main__':
    main()
