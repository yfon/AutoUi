

"""
创建角色页面
"""
from selenium.webdriver.common.by import By

from base_page.base_page import BasePage
from base_page.common_search import CommonButtons


class RolePage(BasePage,CommonButtons):
    data_path = '../test_datas/role_infor.yaml'
    #basci_mag = (By.XPATH, '//div[@id="app"]/div/div[2]/div[1]/div[1]/ul/div/div[10]/li/div/span')
    role_mag = (By.XPATH, '//div[@id="app"]/div/div[2]/div[1]/div[1]/ul/div/div[7]/li/ul/div[3]/li/span')
    create_role_button = (By.XPATH, '//div[@id="app"]/div/div[2]/div[2]/section/div[1]/div/div[1]/div/div[1]/div/div/div[2]/span/button')
    role_name = (By.XPATH, '//div[@aria-label="创建"]/div[2]/form/div[1]/div/div[1]/input')
    role_style = (By.XPATH, '//div[@aria-label="创建"]/div[2]/form/div[2]/div/div/div[1]/input')
    role_value = (By.XPATH , '/html/body/div[last()]/div/div/ul/li[1]')
    role_description = (By.XPATH, '//div[@aria-label="创建"]/div[2]/form/div[3]/div/div/textarea')
    saveC_button = (By.XPATH,'//div[@aria-label="创建"]/div[last()]/div/span[2]/button')
    def create_role(self,role_name,role_description):
        self.wait(1)
        self.click(self.basic_management)
        self.wait(1)
        self.click(self.role_mag)
        self.wait(3)
        self.click(self.create_role_button)
        self.input(self.role_name,role_name)
        self.click(self.role_style)
        self.wait(0.5)
        self.click(self.role_value)
        self.input(self.role_description,role_description)
        self.click(self.saveC_button)
    def edit_role(self,role_name):
        self.wait(1)
        self.input(self.search_input,role_name)
        self.click(self.saveC_button)

