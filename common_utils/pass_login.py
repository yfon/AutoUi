# ******************
# 通过cookie登录网站
# ******************
import pickle

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import json
from time import sleep, time
from datetime import datetime
import os


class Test_loggin(object):

    def __init__(self, log_url, cas_url, cookie_path,service_url, yuanshu, cookie_name='cookies.pkl', expiration_time=30):
        '''
        :param log_url: 登录网址
        :param home_url: 首页网址
        :param cookie_path: cookie文件存放路径
        :param yuanshu: 进入主页后验证的元素
        :param cookie_path: 文件命名
        :param expiration_time: cookie过期时间,默认30分钟
        '''
        self.log_url = log_url
        self.cas_url = cas_url
        self.service_url = service_url
        self.cookie_path = cookie_path
        self.yuanshu = yuanshu
        self.cookie_name = cookie_name
        self.expiration_time = expiration_time

    def get_cookie(self):
        '''手动登录获取cookie'''
        driver = webdriver.Chrome()
        driver.get(self.log_url)
        print('第一次登录进入界面得cookie')
        print(driver.get_cookies())
        driver.maximize_window()
        # 显性等待2，当页面出现某个元素时就执行下列的操作
        WebDriverWait(driver, 60, 2).until(lambda x: x.find_element_by_xpath(self.yuanshu))
        # driver.get(self.cas_url)
        print('第一次登录跳转到cas得cookie')
        pickle.dump(driver.get_cookies(), open(os.path.join(self.cookie_path, self.cookie_name), "wb"))
        print('第一次进入cas得cookie，bing存入文件中得cookie')
        print(driver.get_cookies())
        driver.close()

    def pd_Cookie(self):
        '''获取最新的cookie文件，判断是否过期'''
        cookie_list = os.listdir(self.cookie_path)  # 获取目录下所有文件
        if not cookie_list:  # 判断文件为空时，直接执行手动登录
            self.get_cookie()
        else:
            cookie_list2 = sorted(cookie_list)  # 升序排序文件,返回新列表；sort是对原列表进行排列
            new_cookie = os.path.join(cookie_path, cookie_list2[-1])  # 获取最新cookie文件的全路径

            file_time = os.path.getmtime(new_cookie)  # 获取最新文件的修改时间，返回为时间戳1590113596.768411
            t = datetime.fromtimestamp(file_time)  # 时间戳转化为字符串日期时间
            print('当前时间：', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print('最新cookie文件修改时间：', t.strftime("%Y-%m-%d %H:%M:%S"))
            date = (datetime.now() - t).seconds // 60  # 时间之差，seconds返回相距秒数//60,返回分数
            print('相距分钟:{0}分钟'.format(date))
            if date > self.expiration_time:  # 默认判断大于30分钟，即重新手动登录获取cookie
                print("cookie已经过期，请重新手动登录获取")
                return self.get_cookie()
            else:
                print("cookie未过期")

    def cookie_loggin(self):
        caslogin_url = 'https://172.18.2.113:8443/cas/login'
        '''自动登录操作'''
        self.pd_Cookie()  # 首先判断cookie是否已获取，是否过期
        print("自动登录开始...")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.log_url)
        print('未过期时候得进入ui-cas得cookie')
        print(driver.get_cookies())
        driver.delete_all_cookies()  # 清除旧cookies
        print('执行过清除浏览器缓存后得cookie')
        cookies = pickle.load(open(os.path.join(self.cookie_path, self.cookie_name), "rb"))
        print('从文件中读出得cookie')
        print(cookies)

        # for cookie in cookies:
            # driver.add_cookie(cookie)
            # driver.add_cookie()

        driver.add_cookie({'name': 'service', 'value': 'https%253A%252F%252F172.18.2.113%253A8443%252Fui-infra%252Fcas%252Fvalidate%26sn'})
        driver.add_cookie({'name': 'InfraToken','value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpblR5cGUiOiJiYXNpYyIsInVzZXJfbmFtZSI6ImFkbWluIiwidXNlcl9zb3VyY2UiOiJBRE1JTiIsImNhc0NsaWVudEFkZHIiOiIxNzIuMTguMC4xNDAiLCJhdXRob3JpdGllcyI6WyJQQU5fQURNSU4iLCJST0xFX0FETUlOIiwiTThDTVBBZG1pbkF1ZGl0b3IiLCJST0xFX1VTRVIiXSwiY2xpZW50X2lkIjoicmRjIiwidGltZV9vdXQiOjE4MDAwLCJsaWNlbnNlIjoibWFkZSBieSBtOCIsInVzZXJfaWQiOjEsImxvZ2luX3RpbWUiOjE2MTg0NjEzNTcwNjksInNjb3BlIjpbInNlcnZlciJdLCJleHAiOjE2MTg0OTczNTcsImRlcHRfaWQiOjEsImN1c3RfaWQiOm51bGwsImp0aSI6Ijc5NGQzMGZlLTgwMzAtNGRkYS1hY2VhLTdkMWRjNzI1NDZmNyJ9.-vaPfGpltJM5CM4pw12hV1YjGf_3UjD2TjkiQ4KJtGs'})
        driver.add_cookie({'name': 'JSESSIONID',
                           'value': 's%3A5ZhvljFE0Y_WWw_uaeGY7k4DSFHGzUMW.o8GilUKoPvr9NT%2FiY1ZGtFexhDhby25ujLd8DFHK6A0'})
            # if cookie['path'] == '/ui-infra':
            #     cookie['path'] = '/cas'



        driver.get(self.service_url)
        sleep(2)
        driver.close()
        print("浏览器退出")


if __name__ == "__main__":
    log_url = 'https://172.18.2.113:8443/cas/login?service=https%3A%2F%2F172.18.2.113%3A8443%2Fui-infra%2Fcas%2Fvalidate&sn=/ui-infra'
    cas_url = 'https://172.18.2.113:8443/cas/env'
    service_url = 'https://172.18.2.113:8443/ui-infra/#/application/microservice'
    cookie_path = 'D:/python_file/cookies'
    yuanshu = '//span[text()="微应用管理"]'

    test_loggin = Test_loggin(log_url=log_url, cas_url=cas_url, service_url=service_url, cookie_path=cookie_path,
                              yuanshu=yuanshu)
    test_loggin.cookie_loggin()