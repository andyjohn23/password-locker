import unittest
from credentials import user_credentials
from user import Users


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
        self.assertEqual(len(user_credentials.user_credential_list), 2)

    def test_user_details_exists(self):
        """
        test to check if we can return a Boolean  if we cannot find the user details.
        """
        self.new_user_details.save_user_details()
        test_user = user_credentials("andrewj","Instagram","andyj","andyj12") # new user details
        test_user.save_user_details()

        user_detail_exists = user_credentials.checking_user_details("andrewj", "andyj12")

        self.assertTrue(user_detail_exists)

    
      
if __name__ == '__main__':
    unittest.main()


