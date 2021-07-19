from ddt import ddt, file_data

from common_utils.get_driver import GetDriver
from pages.login_page import LoginPage
import unittest

import yaml

from pages.mic_page import MicPage


@ddt
class MicTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver('Chrome')
        cls.lg = LoginPage(cls.driver)
        cls.mic = MicPage(cls.driver)
        cls.lg.login_in()
        cls.mic_infor = cls.mic.open_yaml()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        # pass

    def test_1_createService(self):

        self.mic.create_mic(self.mic_infor[0]['create_data']['mic_name'], self.mic_infor[0]['create_data']['mic_code'],
                            self.mic_infor[0]['create_data']['mic_path'])
        # print(mic_infor)
        # self.mic.edit_mic(mic_infor[0]['create_data']['mic_name'], mic_infor[0]['edit_data']['mic_name'])
        # self.mic.delete_mic(mic_infor[0]['edit_data']['mic_name'])

    def test_2_editService(self):
        # print(mic_infor)
        self.mic.edit_mic(self.mic_infor[0]['create_data']['mic_name'], self.mic_infor[0]['edit_data']['mic_name'])

    def test_3_delService(self):
        self.mic.delete_mic(self.mic_infor[0]['edit_data']['mic_name'])
if __name__ == '__main__':
    unittest.main()
