#-*-coding: UTF-8 -*-
'''
Created on 2019年12月12日
@author: LIJY
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ele_loc import homepage_loc
from ele_loc import back_loc
from testdata import common_data
from common.basepage import BasePage
from common.rand_name import random_name
from testdata import bid_data
import time


# 点击抢投标
class Backpage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.implicitly_wait(10)
        
    def login(self):
        # 输入用户名，密码和万能验证码登录
        self.driver.get(common_data.back_url)
        self.input_text(back_loc.username_loc, common_data.back_username, "后台输入用户名")
        self.input_text(back_loc.pwd_loc, common_data.back_pwd, "后台输入密码")
        self.input_text(back_loc.verify_loc, common_data.back_verify_code, "后台输入万能验证码")
        self.ele_click(back_loc.login_btn_loc, "点击后台登录按钮")
        
        
    def add_bid(self,amount=100000,days=30,rate=10,term=1,):
        # 随机产生标的名称
        title = random_name()
        self.ele_click(back_loc.loan_manage_loc, "点击贷款管理")
        
        self.switch_to_iframe(back_loc.add_bid_iframe_loc, "切换iframe")
        time.sleep(2)
        
        self.ele_click(back_loc.add_bid_loc, "点击加标按钮")
        self.input_text(back_loc.loaner_name_loc, common_data.loaner_phone, "输入借款人手机号")
        time.sleep(0.5)
#         self.set_attr(back_loc.loaner_name_hide_loc, "value", common_data.loaner_name, "隐藏控件输入借款人姓名")
        self.ele_click(back_loc.chose_loaner_loc, "选择借款人")
        self.input_text(back_loc.bid_title_loc, title, "输入标的名称")
        self.input_text(back_loc.bid_rate_loc, rate, "输入利率/月")
        self.input_text(back_loc.bid_term_loc, term, "输入期限")

        self.input_text(back_loc.bid_amount_loc, amount, "输入贷款金额")
        self.input_text(back_loc.bid_days_loc, days, "输入竞标时长/天")
        self.ele_click(back_loc.evalue_leaf_loc, "点击风险测评按钮")
        self.input_text(back_loc.evalue_amount_loc, "1", "输入评估价值为1")
        self.ele_click(back_loc.proj_loc, "项目录入页签点击")
        self.input_text(back_loc.native_loc, "中国", "输入籍贯")
        self.input_text(back_loc.profession_loc, "老赖", "输入职业")
        self.input_text( back_loc.Age_loc, "18", "输入年龄")
        self.ele_click(back_loc.bid_submit_loc, "提交新建标的")
        # 用新产生的标的名称，复制给标的数据
        return title
        
        
    def audit_bid(self):
        # 做三遍审核操作
        for i in range(0,3):
            time.sleep(2)
            self.ele_click(back_loc.newest_bid_loc, "点击最新一条标的")
            self.ele_click(back_loc.audit_loc, "点击审核")
            self.ele_click(back_loc.pass_loc, "审核通过")
        
        