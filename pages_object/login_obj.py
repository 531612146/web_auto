#-*-coding: UTF-8 -*-
'''
Created on 2019年12月2日
@author: LIJY
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ele_loc import login_loc as loc
from testdata import common_data
from common.basepage import BasePage


class Login(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(common_data.login_url)
        self.driver.implicitly_wait(10)
        
    def login(self,username,pwd):
        # 输入账号名，密码，点击登录
        
        self.input_text(loc.username_loc, username, "登录页面输入用户名")
        self.input_text(loc.pwd_loc,pwd,"登录页面输入密码")
        self.ele_click(loc.submit_loc, "点击登录按钮")
        
    # 登录成功返回True,失败返回false    
    def is_successed(self):
        try:
            self.wait_until_visible(loc.logout_loc, "等待登录页面退出链接可见")
            return True
        except:
            return False
        
    # 返回页面中间的错误信息
    def dia_errmsg(self):
        return self.get_text(loc.dia_errmsg_loc, "获取登录页面中间错误信息返回值")
        
    # 返回账号密码输入框下的格式校验错误信息
    def form_errmsg(self):
        return self.get_text(loc.form_errmsg_loc, "获取登录页面的用户名密码输入框下的错误信息")
