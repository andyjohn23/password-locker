import string
import random
from user import Users


class user_credentials:
    """class for storing user credentials"""

    user_credential_list = []

    @classmethod
    def checking_user_details(cls, username, password):
        """Class method to check if user details match"""
        registered_users = ""
        for user in Users.users_list:
            if (user.username == username and user.password == password):
                registered_users = user.username
        return registered_users

    def __init__(self, username, social_network, account_name, password):
        self.username = username
        self.social_network = social_network
        self.social_network_username = account_name
        self.password = password

    def save_user_details(self):
        """saving user information"""
        user_credentials.user_credential_list.append(self)

    def delete_user_details(self):
        """deleting user infromation"""
        user_credentials.user_credential_list.remove(self)

  
    def automatic_generated_password(length=12, password=string.digits+string.ascii_letters+string.ascii_uppercase):
        """Function to generate a random password"""

        random_password = ''.join(random.choice(password) for i in range(length))
        return random_password


    @classmethod
    def display_user_details(cls, username):
        """Class method to show user details"""
        user_credential_list = []
        for user_details in cls.user_credential_list:
            if user_details.username == username:
                user_credential_list.append(user_details)
        return user_credential_list
