#-*-coding: UTF-8 -*-
'''
Created on 2019年12月10日
@author: LIJY
'''
from selenium.webdriver.common.by import By

# 投标页面
# 标的剩余金额/万元
bid_remain_loc = (By.XPATH,'//span[@class="mo_span4"]')

# 投资金额输入框,用户剩余金额为该元素中的一个属性
bid_amount_loc = (By.XPATH,'//input[contains(@class,"invest-unit-investinput")]')

# 剩余投资时间 天/时/分/秒span，四个元素
bid_countdown_loc = (By.XPATH,'//span[contains(@class,"clock-img")]/following-sibling::span/span')

# 投标按钮
bid_button_loc = (By.XPATH,'//button[text()="投标"]')
 
# 页面中间报错弹框
bid_err_dia_loc = (By.XPATH,'//div[@class="text-center"]')

# 投资成功页面的查看按钮,点击切换到个人页面时间比较长
scss_view_button_loc = (By.XPATH,'//button[text()="查看并激活"]')






 
 



