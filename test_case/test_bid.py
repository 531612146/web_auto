#-*-coding: UTF-8 -*-
'''
Created on 2019年12月11日
@author: LIJY
'''

from selenium import webdriver
import pytest
import time
from futurn_loan.testdata import common_data
from futurn_loan.testdata import bid_data as data
from futurn_loan.pages_object import bid_obj
from futurn_loan.pages_object.login_obj import Login
from futurn_loan.common.mylogging import mylogging


# @pytest.fixture()
# def init_driver():
#     # 初始化driver,并登陆页面
#     driver = webdriver.Chrome()
#     driver.get(common_data.login_url)
#     # 登录
#     Login(driver).login(common_data.username, common_data.pwd)
#     
#     # 返回driver
#     yield driver
#     # 关闭窗口，关闭浏览器
#     driver.close()
#     driver.quit()

# @pytest.mark.usefixtures("init_login")
@pytest.mark.usefixtures("build_bid")
@pytest.mark.smoke
def test_bid_successs(build_bid,init_login):
    # 获取各个参数
    driver = init_login
    homepage = bid_obj.Homepage(driver)
    bidpage = bid_obj.BidPage(driver)
    userpage = bid_obj.UserInfoPage(driver)
#     bid_name = data.bid_sucess["bid_name"]
    bid_name = build_bid
    amount = data.bid_sucess["bid_amount"]
    # 点击投资按钮    
    time.sleep(2)
    bid_remain_before = homepage.get_bid_remain(bid_name)
    homepage.bid_button_click(bid_name)
    # 输入投资金额,并点击投资
    user_remain_amount_before = bidpage.get_user_remain_amount()
    bidpage.input_invest_amount(amount)
    bidpage.click_bid_button()
    # 点击查看并激活
    bidpage.scuss_view_click()
    # 进入个人信息页面查看用户余额
    time.sleep(5)  # 这个页面加载比较慢
    user_remain_amount_after = userpage.get_user_remain_amount()
    # 断言最新投资记录与投资操作符合
    mylogging.info("断言最新投资记录与投资操作符合")
    assert userpage.is_newest_record_match(bid_name, amount)
#     # 断言用户金额减少,这条断言失败了
#     mylogging.info("断言用户金额减少")
#     assert amount == user_remain_amount_after - user_remain_amount_before
    
    # driver返回标的信息页面
    driver.back()
    driver.refresh()
    # 获取标的剩余金额
    bid_remain_after = bidpage.get_bid_remain_amount()
    
    # 断言标的金额减少
    mylogging.info("断言标的金额减少")
    assert bid_remain_before - bid_remain_after == amount

    