"""
-- coding: utf-8 --
@Time : 2020/6/1 17:04
@Author : jcoool
@Site : 
@File : index_locator.py
@Software: PyCharm
"""
from selenium.webdriver.common.by import By


class IndexLocator:
    """大屏的元素定位"""
    # 定位配置中心
    user_info = (By.XPATH, '//span[text()="配置中心"]')
    # # 退出登录
    # quit_btn = (By.XPATH, "//a[text()='退出']")

