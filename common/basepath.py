#-*-coding: UTF-8 -*-
'''
Created on 2019年12月9日
@author: LIJY
'''


import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目目录
output_path = os.path.join(base_path,"output")  # 输出文件目录
report_path = os.path.join(output_path,"report")  # 测试报告目录
screenshot_path = os.path.join(output_path,"screenshot")  # 屏幕截图文件目录
log_path = os.path.join(output_path,"log")  #  日志文件目录
cfg_file = os.path.join(base_path,"cfg.ini")  # 配置文件目录
allure_path = os.path.join(output_path,"allure")
