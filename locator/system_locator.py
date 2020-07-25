"""
-- coding: utf-8 --
@Time : 2020/6/1 22:11
@Author : jcoool
@Site : 
@File : system_locator.py
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

class SystemLocator():
    """系统配置的元素定位"""
    # 点击系统配置
    click_system = (By.XPATH, '//*[@id="oneLvMenus"]/li[6]')


class system_click_organization():
        # 点击组织架构管理
        click_organization = (By.XPATH,'//*[@id="loadPageDiv"]/div/div[1]/div/div[3]/div/div[1]/div/ul/li[2]')
        # 新增组织架构信息
        new = (By.XPATH,'//*[@id="loadPageDiv"]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/button[1]')
        # 填写组织架构名字
        new_input = (By.XPATH,'//*[@id="loadPageDiv"]/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div/span/span/div/input')
        # 填写组织架构后保存
        new_save = (By.XPATH,'//*[@id="loadPageDiv"]/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/span/button[1]')



