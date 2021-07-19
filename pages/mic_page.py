from base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from base_page.common_search import CommonSearch
"""
微服务页面
"""


class MicPage(BasePage):
    data_path = '../test_datas/mic_infor.yaml'
    # mic = (By.XPATH, '//span[text()="微服务管理"]')
    create_button = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/span/button')
    create_mic_name = (By.XPATH, '//div[@aria-label="创建微服务"]/div[2]/form/div/div/div/input')
    create_mic_code = (By.XPATH, '//div[@aria-label="创建微服务"]/div[2]/form/div[2]/div/div/input')
    create_mic_path = (By.XPATH, '//div[@aria-label="创建微服务"]/div[2]/form/div[3]/div/div/input')
    create_save_button = (By.XPATH, '//div[@aria-label="创建微服务"]/div[3]/span[2]/button')
    # CommonButtons.search_input = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/div/div/div/input')
    # CommonButtons.search_button = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/div/div/span/button')
    edit_button = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/section/div[1]/div/div[2]/div[4]/div[2]/table/tbody/tr/td[10]/div/div/div/span[1]')
    edit_mic_name = (By.XPATH, '//div[@aria-label="编辑微服务"]/div[2]/form/div/div/div/input')
    edit_save_button = (By.XPATH, '//div[@aria-label="编辑微服务"]/div[3]/span[2]/button')
    refresh_button = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/div/div/span[2]/button')
    delete_button = (
    By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/section/div[1]/div/div[2]/div[4]/div[2]/table/tbody/tr/td[10]/div/div/div/span[2]')
    delete_ensure = (By.XPATH, '//div[@aria-label="提示"]/div/div[3]/button[2]')

    def create_mic(self, mic_name, mic_code, mic_path):
        self.webDriverWait(10, 1, self.create_button, '没有找到')
        self.click(self.create_button)
        self.input(self.create_mic_name, mic_name)
        self.input(self.create_mic_code, mic_code)
        self.input(self.create_mic_path, mic_path)
        self.click(self.create_save_button)

    def edit_mic(self, serch_name, edit_name):
        self.input(CommonSearch.search_input, serch_name)
        self.click(CommonSearch.search_button)
        self.wait(1)
        self.click(self.edit_button)
        self.wait(2)
        self.clearInput(self.edit_mic_name)
        self.input(self.edit_mic_name, edit_name)
        self.click(self.edit_save_button)
        self.click(self.refresh_button)

    def delete_mic(self, edit_name):
        self.input(CommonSearch.search_input, edit_name)
        self.click(CommonSearch.search_button)
        self.wait(1)
        self.click(self.delete_button)
        self.click(self.delete_ensure)
        self.click(self.refresh_button)
