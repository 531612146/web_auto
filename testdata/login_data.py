#-*-coding: UTF-8 -*-
'''
Created on 2019年12月3日
@author: LIJY
'''

# 登录成功用户名密码
login_sucess = [{"username":"18684720553","pwd":"python"}]
# 账号未注册/输入密码错误/
wrong_account = [{"username":"13966666666","pwd":"123456","errmsg":"此账号没有经过授权，请联系管理员!"},
                 {"username":"18684720553","pwd":"123456","errmsg":"帐号或密码错误!"},
                 ]


# 手机号格式不正确/手机号为空/密码为空
invalid_input = [{"username":"1868472","pwd":"123456","errmsg":"请输入正确的手机号"},
                 {"username":"","pwd":"123456","errmsg":"请输入手机号"},
                 {"username":"18684720553","pwd":"","errmsg":"请输入密码"}                
                 ]



