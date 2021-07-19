# 继承基类
import configparser
import os
import time

import yaml
from selenium.webdriver.common.by import By

# 定义登录页面类
from base_page.base_page import BasePage
from common_utils.get_driver import GetDriver

"""
登录界面
"""


class LoginPage(BasePage):
    url_filepath = '../config/url.ini'
    url_config = configparser.RawConfigParser()
    url_config.read(url_filepath, encoding="utf-8")
    url = url_config.get("db_item", "url")
    # url = 'http://172.18.2.113:8443/cas/login?service=https%3A%2F%2F172.18.2.113%3A8443%2Fui-infra%2Fcas%2Fvalidate&sn=/ui-infra'
    # 页面元素
    name = (By.ID, 'username')
    password = (By.XPATH, '//div[@id="ccs-app"]/div/div/div[3]/input')
    button = (By.XPATH, '//div[@id="ccs-app"]/div/div/button')
    data_path = '../test_datas/login_user.yaml'

    def login_in(self):
        yaml_data = self.open_yaml()
        self.open()
        # self.wait(5)
        self.input(self.name, yaml_data[0]['username'])
        self.input(self.password, yaml_data[0]['password'])
        self.click(self.button)


if __name__ == '__main__':
    lg = LoginPage(GetDriver('Chrome'))
    # lg.login()
    lg.login_in()
