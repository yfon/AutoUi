import unittest

from ddt import ddt, file_data

from common_utils.get_driver import GetDriver
from pages.login_page import LoginPage
from pages.role_page import RolePage

@ddt
class RoleTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver('Chrome')
        cls.lg = LoginPage(cls.driver)
        cls.role = RolePage(cls.driver)
        cls.lg.login_in()
    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass
    # @file_data('../test_datas/role_infor.yaml')
    # def test_role(self,**kwargs):
    #     self.role.create_role(kwargs['rolename'],kwargs['roledescription'])
    def test_role(self):
        role_infor = self.role.open_yaml()
        self.role.create_role(role_infor[0]['create_role']['rolename'], role_infor[0]['create_role']['roledescription'])
        self.role.edit_role(role_infor[0]['edit_role']['rolename'])

if __name__ == '__main__':
    unittest.main()
