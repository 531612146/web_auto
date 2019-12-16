#-*-coding: UTF-8 -*-
'''
Created on 2019年12月12日
@author: LIJY
'''
from selenium.webdriver.common.by import By

# 后台登录页面姓名输入框
username_loc = (By.XPATH,'//input[@name="admin_name"]')
# 后台登录页面密码输入框
pwd_loc = (By.XPATH,'//input[@name="admin_pwd"]')
# 后台登录页面验证码输入框
verify_loc = (By.XPATH,'//input[@name="code"]')
# 登录按钮
login_btn_loc = (By.XPATH,'//button[contains(@class,"admin_login_btn")]')
# 后台借款管理菜单
loan_manage_loc = (By.XPATH,'//span[text()="借款管理"]')


# 加标按钮所在iframe
add_bid_iframe_loc = (By.XPATH,'//iframe[@id="mainFrame"]')
# 后台加标按钮
add_bid_loc = (By.XPATH,'//span[text()="加标"]')
# 加标信息页面,借款人姓名
loaner_name_loc = (By.XPATH,'//input[@placeholder="输入手机号码进行查找"]')

# # 加标信息页面借款人隐藏信息
# loaner_name_hide_loc =(By.XPATH,'//input[@name="RegName"]')
# 借款人名字所在行
chose_loaner_loc = (By.XPATH,'//tr[@id="datagrid-row-r2-2-0"]')
# 标的名称输入框
bid_title_loc = (By.XPATH,'//input[contains(@class,"validatebox-invalid") and @name="Title"]')

# 标的年利率输入框
bid_rate_loc = (By.XPATH,'//input[@name="LoanRate"]')

# 标的时间输入框
bid_term_loc = (By.XPATH,'//input[@name="LoanTerm"]')

# 标的额度输入框
bid_amount_loc = (By.XPATH,'//input[@name="Amount"]')

# 竞标时间输入框
bid_days_loc =(By.XPATH,'//input[@name="BiddingDays"]')

# 提交按钮
bid_submit_loc = (By.XPATH,'//span[text()="提交"]')


# 切换风控评测页签
evalue_leaf_loc = (By.XPATH,'//span[text()="风控评测"]/parent::a')
# 评估价值输入框
evalue_amount_loc =(By.XPATH,'//input[@name="EvaluAmount"]')

# 项目录入输入框
proj_loc = (By.XPATH,'//span[text()="项目录入"]/parent::a')
# 籍贯输入框
native_loc = (By.XPATH,'//input[@name="Native"]')
# 职业输入框
profession_loc = (By.XPATH,'//input[@name="Profession"]')
# 年龄输入框
Age_loc = (By.XPATH,'//input[@name="Age"]')

# 标的列表第一条记录
newest_bid_loc = (By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]')

# 审核按钮
audit_loc = (By.XPATH,'//span[text()="审核"]')

# 审核通过按钮
pass_loc = (By.XPATH,'//span[text()="审核通过"]')

# 核保审批按钮 = 
check_audit_loc = (By.XPATH,'//span[text()="核保审批"]')






