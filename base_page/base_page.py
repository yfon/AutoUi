"""
  pom的基类 对操作二次封装，就说关键字驱动设计模型的KEY_word 层
"""
import yaml
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as  EC
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def open_yaml(self):
        user_file = open(self.data_path, 'r', encoding='utf-8')
        yaml_data = yaml.load(user_file.read(), Loader=yaml.FullLoader)
        user_file.close()
        return yaml_data

    # 访问地址
    def open(self):
        self.driver.get(self.url)

    # 元素定位。单个元素
    def locator(self, loc):
        # 采用的是封装的定位方式  find_element(By.ID,value)
        return self.driver.find_element(*loc)

    # 元素定位，多个元素
    def locators(self, loc):
        return self.driver.find_elements(*loc)

    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 显示等待  waitTime-->等待时间、defaultPoll-->
    # 寻找某个元素，如果没有找到就打印出相应的信息
    def webDriverWait(self, waitTime, defaultPoll, loc, message):
        WebDriverWait(self.driver, waitTime, defaultPoll).until(EC.presence_of_element_located(loc), message=message)

    # 隐式等待,等待所有的元素
    def implicitlyWait(self, waitTime):
        self.driver.implicitly_wait(waitTime)

    # 强制等待
    def wait(self, waitTime):
        sleep(waitTime)

    # # 退出
    def quit(self):
        self.driver.quit()

    # 清除input数据
    def clearInput(self, loc):
        loc = self.locator(loc)
        loc.click()  # 点击这个文本框
        loc.send_keys(Keys.CONTROL, "a")  # 键盘操作，control+a
        loc.send_keys(Keys.DELETE)


    def getJs(self, elementId):
        js = 'document.getElementById("' + elementId + '")'
        return js

    # 不可用元素处理  使用js--》disable
    # js = document.getElementById('ss').removeAttribute('disabled')
    # 移除属性
    def removeAttribute(self, elementId,attribute):
        js = self.getJs(elementId) + '.removeAttribute("'+attribute+'")'
        self.driver.execute_script(js)

    # 不可见元素处理  style="display:none"
    def removeDisplayNone(self, elementId):
        js = self.getJs(elementId) + '.style.display=""'
        self.driver.execute_script(js)

    # 窗口滑动
    def scrollWindown(self, px1, px2):
        js = 'window.scrollTo(' + px1+','+ px2 + ')'
        self.executeJs(js)



    # 判断是否被选中is_selected()
    def isSelected(self, loc):
        try:
            self.locator(loc).is_selected()
            return 'selected'
        except Exception as e:
            print('not selected', format(e))
