#-*-coding: UTF-8 -*-
'''
Created on 2019年12月12日
@author: LIJY
'''

import pytest
from common import rand_name
from testdata import common_data
from selenium import webdriver
from pages_object import back_obj
from common.mylogging import mylogging




@pytest.fixture
def build_bid(scope="session",autouse=True):
    mylogging.info("session级别前置build_bid开始...")
    driver = webdriver.Chrome()
    back = back_obj.Backpage(driver)
    back.login()
    title = back.add_bid('100000')
    back.audit_bid()
    driver.quit()
    # 返回新建的标的名称
    yield title
    mylogging.info("session级别前置build_bid结束...")