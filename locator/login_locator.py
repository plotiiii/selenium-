"""
-- coding: utf-8 --
@Time : 2020/6/1 16:09
@Author : jcoool
@Site : 
@File : login_locator.py
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

class LoginLocator():
    """登录页面的元素定位,私密连接的元素定位"""
    # 高级
    senior = (By.XPATH, "//*[@id='details-button']")
    # 继续前往
    travel = (By.XPATH, '//*[@id="proceed-link"]')
    # 账号输入框
    user_loc = (By.XPATH,'//input[@placeholder="账号"]')
    # 账号输入框
    pwd_loc = (By.XPATH, '//input[@placeholder="密码"]')
    # 登录按钮
    login_loc = (By.XPATH,'//*[@id="app"]/section/main/div/div[3]/div[3]/form/button')
