"""
-- coding: utf-8 --
@Time : 2020/6/1 22:23
@Author : jcoool
@Site : 
@File : page_organization.py
@Software: PyCharm
"""

from wanwoo.common.base_page import BasePage
from wanwoo.locator.system_locator import SystemLocator, system_click_organization


class OrganizationPage(BasePage):
    """组织架构操作相关操作"""

    def click_system(self):
        self.click_element(SystemLocator.click_system, '点击配置中心的系统设置')

    def click_equipment(self):
        self.click_element(system_click_organization.click_organization, '点击系统配置-组织架构管理')

    def new_organization(self, organization_name):
        """新增一个组织架构"""
        self.click_element(system_click_organization.new, '组织架构管理-新增')
        self.input_text(system_click_organization.new_input, organization_name, '组织架构管理-填写分组名')
        self.click_element(system_click_organization.new_save, '组织架构管理-保存')
