"""
-- coding: utf-8 --
@Time : 2020/6/1 16:20
@Author : jcoool
@Site : 
@File : page_login.py
@Software: PyCharm
"""
from selenium.webdriver.remote.webdriver import WebDriver

from wanwoo.common.base_page import BasePage
from wanwoo.common.handle_config import conf
from wanwoo.locator.login_locator import LoginLocator as loc


class LoginPage(BasePage):
    """登录页面"""
    # 登录的url地址
    url = conf.get('env', 'base_url')

    # url = 'http://120.78.128.25:8765/Index/login.html'

    def __init__(self, driver):
        """
        :param driver: webdriver对象
        :type driver: WebDriver
        """
        super().__init__(driver)
        # 打开登录页面
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)

    def login(self, user, pwd):
        """输入账号密码点击登录"""
        # 高级
        self.click_element(loc.senior, '私密连接_高级')
        # 继续前往
        self.click_element(loc.travel, '私密连接_继续前往')
        self.input_text(loc.user_loc, user, '登录_账号输入')
        # 输入密码
        self.input_text(loc.pwd_loc, pwd, '登录_密码输入')
        # 点击登录
        self.click_element(loc.login_loc, '登录_点击元素')
