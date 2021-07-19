import unittest

from common_utils.get_driver import GetDriver
from pages.application_page import ApplicationPage
from pages.login_page import LoginPage


class ApplicationTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver('Chrome')
        # cls.lg = LoginPage(cls.driver)
        cls.application = ApplicationPage(cls.driver)
        # cls.lg.login_in()
        # cls.applicaiton_infro = cls.application.open_yaml()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
        # cls.driver.quit()

    @unittest.skip
    def test_dev_applicaiton(self):
        self.application.creat_dev_application(self.applicaiton_infro[0]["dev_application"]["dev_name"],
                                               self.applicaiton_infro[0]["dev_application"]["mic_code"])
        self.application.edit_dev_application(self.applicaiton_infro[0]["dev_application"]["dev_name"],
                                              self.applicaiton_infro[0]["edit_data"]["dev_name"])
        self.application.delete_dev_application(self.applicaiton_infro[0]["edit_data"]["dev_name"])
        # self.assertEqual()
    @unittest.skip
    def test_user_application(self):
        self.application.create_user_application(self.applicaiton_infro[0]['user_application']['name'],self.applicaiton_infro[0]['user_application']['code'])
        self.application.edit_user_application(self.applicaiton_infro[0]['user_application']['name'],self.applicaiton_infro[0]['edit_user_data']['name'])
        self.application.delete_user_applicaiton(self.applicaiton_infro[0]['edit_user_data']['name'])
    def test_testda(self):
        self.application.testda()
if __name__ == '__main__':
    unittest.main()
