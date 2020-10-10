import pickle
import random
import string

class Users:
    """A class that generates new instances of Users"""
    users_list = []  # Empty Users list

    def __init__(self, username, email, password):
        """instance variable unique to each instance"""

        self.username = username  # new username
        self.email = email  # new emailaddress
        self.password = password  # new password

    def save_users_details(self):
        """saving users details to the users list"""

        Users.users_list.append(self)



        