from selenium.webdriver.common.by import By

from base_page.base_page import BasePage
from base_page.common_search import CommonButtons
from common_utils.log import Logger
"""
    创建用户界面
"""

class UserPage(BasePage,CommonButtons):
    logger = Logger()
    data_path = '../test_datas/user_infor.yaml'
    # basci_mag = (By.XPATH, '//span[text()="基础管理"]')
    user_mag = (By.XPATH, '//div[@id="app"]/div/div[2]/div[1]/div[1]/ul/div/div[7]/li/ul/div[1]/li/span')
    create_user_button = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/span/button')
    create_nickname = (By.XPATH, '//div[@aria-label="创建"]/div[2]/div/form/div[1]/div/div/input')
    create_name = (By.XPATH, '//div[@aria-label="创建"]/div[2]/div/form/div[2]/div/div/input')
    create_tele = (By.XPATH, '//div[@aria-label="创建"]/div[2]/div/form/div[3]/div/div/input')
    create_email = (By.XPATH, '//div[@aria-label="创建"]/div[2]/div/form/div[4]/div/div/input')
    create_password = (By.XPATH, '//div[@aria-label="创建"]/div[2]/div/form/div[6]/div/div/input')
    create_bumen = (By.XPATH, '//div[@aria-label="创建"]/div[2]/div/form/div[8]/div/div/div/button')
    choose_bumen_input = (By.XPATH, '//div[@aria-label="选择部门"]/div[2]/div/div/input')
    bumen = (By.XPATH, '//div[@aria-label="选择部门"]/div[2]/div/div[2]/div[3]/div/span[2]')
    create_role = (By.XPATH, '//div[@aria-label="创建"]/div[2]/div/form/div[10]/div/div/div')
    role_data = (By.XPATH, '//div[contains(@class,"is-multiple")]/div/div/ul/li[1]/span[text()="admin"]')
    create_group = (By.XPATH, '//div[@aria-label="创建"]/div[2]/div/form/div[11]/div/div/div')
    # 动态数据，获取最后一个div
    group_data = (By.XPATH,'/html/body/div[last()]/div/div/ul/li[1]')
    create_save_button = (By.XPATH, '//div[@aria-label="创建"]/div[3]/span[2]/button')
    search_user = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/div/div/div/input')
    search_user_button = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/div/div/div/div/span/button')
    edti_user_button = (By.XPATH,'//section[@class="app-main"]/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[last()]/div/div/span')
    edit_nickname_input = (By.XPATH, '//div[@aria-label="编辑"]/div[2]/div/form/div[1]/div/div/input')
    edit_save_button = (By.XPATH, '//div[@aria-label="编辑"]/div[3]/span[2]/button')
    refresh_button = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/div/span/button')
    delete_user_button = (By.XPATH, '//section[@class="app-main"]/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[last()]/div/div/span[2]')
    ensure_button = (By.XPATH, '//div[@aria-label="提示"]/div/div[3]/button[2]')
    def create_user(self, nickname, name, tele, email, password, bumen):
        self.wait(1)
        self.click(self.basic_management)
        self.wait(0.5)
        self.click(self.user_mag)
        self.wait(1)
        self.click(self.create_user_button)
        self.input(self.create_nickname, nickname)
        self.input(self.create_name, name)
        self.input(self.create_tele, tele)
        self.input(self.create_email, email)
        self.input(self.create_password, password)
        self.click(self.create_bumen)
        self.wait(1)
        self.input(self.choose_bumen_input, bumen)
        self.wait(1)
        self.click(self.bumen)
        # 移动到可见元素
        # target = self.locator(self.create_nickname)
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.wait(1)
        self.click(self.create_role)
        self.click(self.role_data)
        self.click(self.create_group)
        self.wait(0.5)
        self.click(self.group_data)
        self.click(self.create_save_button)
    def edit_user(self,username,edit_nickname):
        self.wait(1)
        self.input(self.search_user,username)
        self.click(self.search_user_button)
        self.click(self.edti_user_button)
        self.wait(0.5)
        self.clearInput(self.edit_nickname_input)
        self.input(self.edit_nickname_input,edit_nickname)
        self.click(self.edit_save_button)
    def delete_user(self):
        self.wait(0.5)
        self.click(self.delete_user_button)
        self.click(self.ensure_button)
        self.click(self.refresh_button)
        self.logger.info('测试')