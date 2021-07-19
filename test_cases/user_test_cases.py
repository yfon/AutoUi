from ddt import ddt, file_data

from common_utils.get_driver import GetDriver
from pages.login_page import LoginPage
import unittest

import yaml

from pages.mic_page import MicPage
from pages.user_page import UserPage


@ddt
class UserTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver('Chrome')
        cls.lg = LoginPage(cls.driver)
        cls.user = UserPage(cls.driver)
        cls.lg.login_in()

    @classmethod
    def tearDownClass(cls) -> None:
        #cls.driver.quit()
         pass

    def test_user(self):
        user_infor = self.user.open_yaml()
        self.user.create_user(user_infor[0]['create_user']['nickname'], user_infor[0]['create_user']['name'],
                            user_infor[0]['create_user']['tele'],user_infor[0]['create_user']['email'],user_infor[0]['create_user']['password']
                              ,user_infor[0]['create_user']['bumen'])
        self.user.edit_user(user_infor[0]['create_user']['nickname'],user_infor[0]['edit_user']['nickname'])
        self.user.delete_user()

if __name__ == '__main__':
    unittest.main()
