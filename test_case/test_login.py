#-*-coding: UTF-8 -*-
'''
Created on 2019年12月3日
@author: LIJY
'''

# from selenium import webdriver
# import unittest
# import ddt
# from futurn_loan.testdata import common_data
# from futurn_loan.testdata import login_data as data
# from futurn_loan.pages_object import login_obj as pages_obj
# 
# @ddt.ddt
# class TestLogin(unittest.TestCase):
#     
#     def setUp(self):
#         # 每个case实例化一个driver
#         self.driver = webdriver.Chrome()
#         # 获取网页地址
#         self.lg = pages_obj.Login(self.driver)
#         
#     def tearDown(self):
#         # 案例执行结束，关闭driver
#         self.driver.close()
#         self.driver.quit()
#         
#     # 登录成功案例  
#     def test_login_sucess(self):
#         self.assertTrue(self.lg.is_successed())
#          
#     # 账号未注册/输入密码错误
#     @ddt.data(*data.wrong_account)
#     def test_login_wrong_account(self,ac):
#         self.lg.login(ac["username"], ac["pwd"])
#         self.assertEqual(ac["errmsg"], self.lg.dia_errmsg())
#      
#     # 手机号格式不正确/手机号为空/密码为空
#     @ddt.data(*data.invalid_input)
#     def test_login_invalid_input(self,ac):
#         self.lg.login(ac["username"], ac["pwd"])
#         self.assertEqual(ac["errmsg"], self.lg.form_errmsg())