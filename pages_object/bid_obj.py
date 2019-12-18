#-*-coding: UTF-8 -*-
'''
Created on 2019年12月10日
@author: LIJY
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ele_loc import homepage_loc
from ele_loc import bid_loc
from ele_loc import userinfo_loc
from testdata import common_data
from common.basepage import BasePage
from common.thousandth_to_str import get_num
import time


# 点击抢投标
class Homepage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)
        
    def bid_button_click(self,bid_name):
        # 首页点击抢投标按钮
        self.ele_click(homepage_loc.bid_loc(bid_name), "首页点击抢投标按钮")
    
    def get_bid_remain(self,bid_name):
        # 获取元素的txt
        txt = self.get_text(homepage_loc.bid_remain_loc(bid_name), "获取首页的标的余额")
        # 获取的txt通过get_num返回float的数值，有万单位会自动*10000
        return get_num(txt)

# 输入金额抢标页面
class BidPage(BasePage):
    def __init__(self,driver):
            super().__init__(driver)
            self.driver = driver
            self.driver.implicitly_wait(10)
    # 输入投资金额
    def input_invest_amount(self,amount):
        self.input_text(bid_loc.bid_amount_loc, amount, "输入投资金额框")
    
    # 投资页面获取用户可用余额
    def get_user_remain_amount(self):
        amount = self.get_attr(bid_loc.bid_amount_loc, "data-amount", "投资页面获取用户余额")
        return get_num(amount)
    
    
    # 获取页面用户可用余额
    def get_bid_remain_amount(self):
        amount = self.get_text(bid_loc.bid_remain_loc, "获取投资页面的标的剩余可投金额")
        return get_num(amount)*10000
    # 点击投标按钮
    def click_bid_button(self):
        self.ele_click(bid_loc.bid_button_loc, "点击投标按钮")
        
    # 获取投标页面中间错误弹框的错误信息
    def get_dia_err_msg(self):
        msg = self.get_text(bid_loc.bid_err_dia_loc,"获取错误弹出框的错误信息")
        return msg
    
    # 获取按钮的文字信息
    def get_bid_button_text(self):
        self.get_text(bid_loc.bid_button_loc, "投标提交按钮获取text值")
    
    # 投资成功，点击查看并激活按钮：
    def scuss_view_click(self):
        ele = self.get_ele(bid_loc.scss_view_button_loc, "点击并查看按钮")
        self.driver.execute_script('arguments[0].onclick()',ele)
    
    # 判断标的是否已到期
    def is_bid_due(self):
        num = 0
        for i in range(1,5):
            time_loc = bid_loc.bid_countdown_loc
            # 在倒计时的Xpath中加入序号，用来分别获取日时分秒
            time_loc[1] = time_loc[1]+'['+str(i)+']'
            text = self.get_text(time_loc, "获取倒计时时分秒")
            # 如果获取时分秒的数值为0，那么num 就+1
            if text == "0":
                num+=1
        # 如果日时分秒全部为零，就返回True,表示已到期
        if num ==4:
            return True
        else:
            return False
        
    # 判断投标按钮是否可用：
    def is_bid_btn_enabled(self):
        self.is_btn_enabled(bid_loc.bid_button_loc, "判断投标按钮是否可用")


class UserInfoPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)
    # 获取用户余额
    def get_user_remain_amount(self):
        return get_num(self.get_text(userinfo_loc.user_useable_loc, "获取用户详情页面用户剩余余额"))
    
    # 获取最新一条投资信息
    def is_newest_record_match(self,invest_name,invest_amount):
        self.ele_click(userinfo_loc.bid_record_button_loc, "点击投资记录按钮")
        invest_date = self.get_text(userinfo_loc.bid_date_loc, "获取最新投资记录的投资日期")
        invest_bid_name = self.get_text(userinfo_loc.bid_record_name_loc, "获取最新投资记录的标的名称")
        bid_amount = get_num(self.get_text(userinfo_loc.bid_amount_loc, "获取最新投资记录的投资金额"))
        nowdate = time.strftime('%Y-%m-%d', time.localtime())
        if invest_name==invest_bid_name and invest_amount == bid_amount and invest_date==nowdate:
            return True
        else:
            return False
        
    
