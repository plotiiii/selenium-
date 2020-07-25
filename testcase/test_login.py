"""
-- coding: utf-8 --
@Time : 2020/6/1 16:40
@Author : jcoool
@Site : 
@File : test_login.py
@Software: PyCharm
"""
import pytest
from selenium import webdriver

from wanwoo.common.handle_config import conf
from wanwoo.common.handle_logging import log
from wanwoo.page.page_login import LoginPage
from wanwoo.page.page_index import IndexPage

@pytest.fixture(scope='class')
def login_fixture():
    """登录功能的前置后置"""
    # 前置条件
    log.info('开始执行登录的用例')
    driver = webdriver.Chrome()
    login_page1 = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page1,index_page
    # 后置条件
    driver.quit()
    log.info('登录的用例执行完毕')


class TestLogin:
    """测试登录"""


    def test_login_pass(self, login_fixture):
        """正常登录的用例"""
        login_page,index_page = login_fixture
        # 进行登录的操作
        login_page.login(conf.get('test_data', 'user'), conf.get('test_data', 'pwd'))
        # 获取登录之后的用户信息
        res = index_page.get_my_user_info()
        # 断言用例执行是否通过
        try:
            assert '登录成功' == res
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")



