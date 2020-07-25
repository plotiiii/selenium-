"""
-- coding: utf-8 --
@Time : 2020/6/1 21:25
@Author : jcoool
@Site : 
@File : page_index.py
@Software: PyCharm
"""
from wanwoo.common.base_page import BasePage
from wanwoo.locator.index_locator import IndexLocator as loc
import time

class IndexPage(BasePage):
    """首页"""

    def get_my_user_info(self):
        """获取我的账户信息"""
        try:
            self.get_element_text(loc.user_info, '大屏_获取配置中心文本')
        except:
            return '登录失败'
        else:
            return '登录成功'

    def click_config(self):
        time.sleep(1.5)
        self.click_element(loc.user_info,'大屏_点击配置中心')