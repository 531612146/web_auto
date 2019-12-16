#-*-coding: UTF-8 -*-
'''
Created on 2019年12月3日
@author: LIJY
'''
from selenium.webdriver.common.by import By


# 用户名输入框
username_loc = (By.XPATH,'//input[@name="phone"]')
# 密码输入框
pwd_loc = (By.XPATH,'//input[@name="password"]')
# 提交按钮
submit_loc = (By.XPATH,'//button[text()="登录"]')
# 首页的退出链接
logout_loc = (By.XPATH,'//a[text()="退出"]')
# 空的手机号和密码/错误的手机号格式，等在手机和密码输入框下的错误提示信息框
form_errmsg_loc = (By.XPATH,'//div[@class="form-error-info"]')
# 账号未注册/密码输入错误dia弹出提示框
dia_errmsg_loc = (By.XPATH,'//div[@class="layui-layer-content"]')



