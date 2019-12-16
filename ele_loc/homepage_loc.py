#-*-coding: UTF-8 -*-
'''
Created on 2019年12月10日
@author: LIJY
'''
from selenium.webdriver.common.by import By

# 首页标的的抢投标按钮,输入标的名称可获取，xpath中标的名称前面有个空格
bid_loc = lambda bid_name:(By.XPATH,'//span[text()=" {}"]/ancestor::div[@class="b-unit"]//a[text()="抢投标"]'.format(bid_name))

# 跳转到首页按钮：
homepage_loc = (By.XPATH,'//a[text()="首页"]')

# 首页标的余额
bid_remain_loc = lambda bidname:(By.XPATH,'//span[text()=" {}"]/ancestor::div[@class="b-unit"]//div[@class="surplus_much"]'.format(bidname))
