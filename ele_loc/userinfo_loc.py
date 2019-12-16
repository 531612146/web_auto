#-*-coding: UTF-8 -*-
'''
Created on 2019年12月10日
@author: LIJY
'''

from selenium.webdriver.common.by import By

# 可用余额
user_useable_loc = (By.XPATH,'//li[@class="color_sub"]')

# 投资项目查看按钮
bid_record_button_loc = (By.XPATH,'//div[text()="投资项目"]')

# 投资记录最新一条投资日期：
bid_date_loc = (By.XPATH,'//div[@ms-controller="tz_list"]//div[@ms-html="item.date"]')

# 投资记录的投资金额
bid_amount_loc = (By.XPATH,'//div[@ms-controller="tz_list"]//div[@ms-html="item.money"]')

# 最新一条投资标的名称
bid_record_name_loc = (By.XPATH,'//div[@ms-controller="tz_list"]//div[@ms-html="item.title"]/a')



