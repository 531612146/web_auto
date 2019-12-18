#-*-coding: UTF-8 -*-
'''
Created on 2019年12月12日
@author: LIJY
'''
from selenium import webdriver
from testdata import common_data
from pages_object import login_obj
import pytest
from common.mylogging import mylogging


@pytest.fixture()
def init_driver():
    # 初始化driver
    mylogging.info("前置initdriver开始...")
    driver = webdriver.Chrome()
    driver.maximize_window()
#     driver.get(common_data.login_url)
    # 返回driver
    mylogging.info("前置initdriver结束...")
    yield driver
    # 关闭窗口，关闭浏览器
    mylogging.info("后置initdriver开始...")
#     driver.close()
#     driver.quit()
    mylogging.info("后置initdriver结束...")

@pytest.fixture    
def init_login(init_driver): 
    mylogging.info("前置init_login开始...")  
    login_obj.Login(init_driver).login(common_data.username, common_data.pwd)
    mylogging.info("后置init_login结束...")
    yield init_driver

    