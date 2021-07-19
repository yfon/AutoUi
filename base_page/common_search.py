from selenium.webdriver.common.by import By


class CommonSearch(object):
    # 基础管理
    basic_management = (By.XPATH, '//div[@id="app"]/div/div[2]/div[1]/div[1]/ul/div/div[7]/li/div')
    # 搜索框
    search_input = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/div/div/div/input')
    # 搜索按钮
    search_button = (By.XPATH, '//section[@class="app-main"]/div/div/div/div/div/div/div/div/span/button')