import pymysql
import win32con
import win32gui
from selenium.webdriver.common.by import By

from base_page.base_page import BasePage
from common_utils.database import DataBase
from common_utils.log import Logger


class ApplicationPage(BasePage):
    logger = Logger()

    image_path = 'D:\\m8sdp\\images\\1.png'
    data_path = '../test_datas/application_infor.yaml'
    application_mag = (By.XPATH, '//span[text()="微应用管理"]')
    reg_dev_application = (
        By.XPATH,
        '//section[@class="app-main"]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/span/button')
    create_dev_app_name = (By.XPATH, '//div[@aria-label="创建开发应用"]/div[2]/form/div/div/div/input')
    create_dev_app_code = (By.XPATH, '//div[@aria-label="创建开发应用"]/div[2]/form/div[2]/div/div/input')
    create_dev_upload = (By.XPATH, '//div[@aria-label="创建开发应用"]/div[2]/form/div[3]/div/div/div[2]/input')
    ensure_dev_application = (By.XPATH, '//div[@aria-label="创建开发应用"]/div[3]/div/span[2]/button')
    search_input = (By.XPATH,
                    '//section[@class="app-main"]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/input')
    search_button = (By.XPATH,
                     '//section[@class="app-main"]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/span[1]/button')
    edit_button = (By.XPATH,
                   '//section[@class="app-main"]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[last()]/div/div/span[1]')
    edit_dev_name = (By.XPATH, '//div[@aria-label="编辑开发应用"]/div[2]/form/div/div/div/input')
    edit_save_button = (By.XPATH, '//div[@aria-label="编辑开发应用"]/div[last()]/div/span[last()]/button')
    delete_button = (By.XPATH,
                     '//section[@class="app-main"]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[last()]/div/div/span[2]')
    refresh_button = search_button = (By.XPATH,
                                      '//section[@class="app-main"]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[1]/span[2]/button')
    delete_ensure = (By.XPATH, '//div[@aria-label="提示"]/div/div[3]/button[2]')
    user_application = (By.XPATH, '//section[@class="app-main"]/div[1]/div/div/div/div/div[1]/div/div/div/div[3]/span')
    user_application_name = (By.XPATH, '//div[@aria-label="创建用户应用"]/div[2]/form/div/div/div/input')
    parent_application = (By.XPATH, '//div[@aria-label="创建用户应用"]/div[2]/form/div[2]/div/div/div/input')
    parent_application_name = (By.XPATH, '//span[text()="平台管理-开发应用"]')
    user_application_code = (By.XPATH, '//div[@aria-label="创建用户应用"]/div[2]/form/div[3]/div/div/input')
    ensure_user_application = (By.XPATH, '//div[@aria-label="创建用户应用"]/div[3]/div/span[2]/button')
    user_search_input = (By.XPATH,
                         '//section[@class="app-main"]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/input')
    user_search_button = (By.XPATH,
                     '//section[@class="app-main"]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div/div[1]/span[1]/button')
    edit_user_button = (By.XPATH,
                   '//section[@class="app-main"]/div[1]/div/div/div/div/div[2]/div[@id="pane-second"]/div/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[last()]/div/div/span[1]')
    edit_user_name = (By.XPATH,'//div[@aria-label="编辑用户应用"]/div[2]/form/div[1]/div/div/input')
    edit_save_button = (By.XPATH,'//div[@aria-label="编辑用户应用"]/div[3]/div/span[2]/button')
    delete_user_button = (By.XPATH,'//section[@class="app-main"]/div[1]/div/div/div/div/div[2]/div[@id="pane-second"]/div/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[last()]/div/div/span[2]')
    def creat_dev_application(self, name, code):
        self.webDriverWait(10, 1, self.application_mag, '没有找到')
        self.click(self.application_mag)
        self.wait(1)
        self.click(self.reg_dev_application)
        self.input(self.create_dev_app_name, name)
        self.input(self.create_dev_app_code, code)
        self.input(self.create_dev_upload, self.image_path)
        self.click(self.ensure_dev_application)

    def edit_dev_application(self, name, editname):
        self.click(self.application_mag)
        self.wait(1)
        self.input(self.search_input, name)
        self.click(self.search_button)
        self.webDriverWait(1, 0.5, self.edit_button, '没有找到编辑按钮')
        self.click(self.edit_button)
        self.webDriverWait(2, 0.5, self.edit_dev_name, '没有找到编辑名称')
        self.clearInput(self.edit_dev_name)
        self.input(self.edit_dev_name, editname)
        self.click(self.edit_save_button)
        self.click(self.refresh_button)

    def delete_dev_application(self, editname):
        self.input(self.search_input, editname)
        self.click(self.search_button)
        self.webDriverWait(2, 0.5, self.delete_button, '')
        self.click(self.delete_button)
        self.click(self.delete_ensure)

    def create_user_application(self, name, code):
        self.webDriverWait(14, 1, self.application_mag, '没有找到')
        self.click(self.application_mag)
        self.webDriverWait(4, 1, self.user_application, '没有找到用户应用tab')
        self.click(self.user_application)
        self.click(self.reg_dev_application)
        self.input(self.user_application_name, name)
        # self.removeAttribute(self.parent_application)
        self.click(self.parent_application)
        self.webDriverWait(4, 1, self.parent_application_name, '没有找到用户应用tab')
        self.click(self.parent_application_name)
        self.input(self.user_application_code, code)
        self.click(self.ensure_user_application)

    def edit_user_application(self, name,editname):
        self.webDriverWait(1,0.5,self.user_search_input,'')
        self.input(self.user_search_input,name)
        self.click(self.user_search_button)
        self.webDriverWait(1, 0.5, self.edit_user_button, '')
        self.click(self.edit_user_button)
        self.webDriverWait(1, 0.5, self.edit_user_name, '')
        self.clearInput(self.edit_user_name)
        self.input(self.edit_user_name,editname)
        self.click(self.edit_save_button)
    def delete_user_applicaiton(self,editname):
        self.webDriverWait(1,0.5,self.user_search_input,'')
        self.clearInput(self.user_search_input)
        self.input(self.user_search_input,editname)
        self.click(self.user_search_button)
        self.webDriverWait(1, 0.5, self.delete_user_button, '')
        self.click(self.delete_user_button)
        self.click(self.delete_ensure)
        self.clearInput(self.user_search_input)
        self.click(self.user_search_button)
    def testda(self):
        db_filepath = '../config/db.ini'
        db_item = 'db'
        sql = 'select * from sys_user'
        dbconfig = DataBase()
        r = dbconfig.excute_sql(db_filepath, db_item,sql)
        print(r)
# # win32gui
#     dialog = win32gui.FindWindow('#32770', '文件上传')  # 对话框
#     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
#     ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
#     Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
#     button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
#
#     win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\all_money.wmv')  # 往输入框输入绝对地址
#     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
