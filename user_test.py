import unittest  # importing the unittest module
from user import Users


class TestUser (unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = Users("andyjohn", "andrewnick906@gmail.com", "andy123")  # create user object

    def test__init__(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "andyjohn")
        self.assertEqual(self.new_user.email, "andrewnick906@gmail.com")
        self.assertEqual(self.new_user.password, "andy123")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Users.users_list = []


    def test_save_users_details(self):
        """
        Test to check if the new users info is saved into the users list
        """
        self.new_user.save_users_details()
        self.assertEqual(len(Users.users_list), 1)

    def test_save_multiple_users(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_users_details()
            test_user = Users("john andy", "johnandy@gmail.com", "john123") # new user
            test_user.save_users_details()
            self.assertEqual(len(Users.users_list),2)

if __name__ == '__main__':
    unittest.main()
