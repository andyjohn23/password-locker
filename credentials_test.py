import unittest
from credentials import user_credentials


class TestUserDetails(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user_details = user_credentials(
            "andyjohn", "Instagram", "andyJohn", "andy123")  # create user details object

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        user_credentials.user_credential_list = []

    def test__init__(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user_details.username, "andyjohn")
        self.assertEqual(self.new_user_details.social_network, "Instagram")
        self.assertEqual(
            self.new_user_details.social_network_username, "andyJohn")
        self.assertEqual(self.new_user_details.password, "andy123")

    def test_save_user_details(self):
        """
        Test to check if the new users info is saved into the users list
        """
        self.new_user_details.save_user_details()
        self.assertEqual(len(user_credentials.user_credential_list), 1)

    def test_save_users_details(self):
        """
        Test to check if the new users details is saved into the users credential list
        """
        self.new_user_details.save_user_details()
        details = user_credentials(
            "andrew", "Facebook", "andrewj", "johnandy1234")  # new user details
        details.save_user_details
        self.assertEqual(len(user_credentials.user_credential_list), 1)

    def test_display_user_details(self):
        """
        Test to check if the display_credentials method, displays the correct credentials.
        """
        self.new_user_details.save_user_details()
        display = user_credentials("johndoe", "Twitter", "doejohn", "john123")
        display.save_user_details()
        display = user_credentials("johndoe", "Twitter", "doejohn", "john123")
        display.save_user_details()
        self.assertEqual(len(user_credentials.display_user_details(display.username)), 2)

if __name__ == '__main__':
    unittest.main()
