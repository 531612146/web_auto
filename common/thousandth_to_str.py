#-*-coding: UTF-8 -*-
'''
Created on 2019年12月10日
@author: LIJY
'''

# 千分位str转换为数据

def filter_num(digit_str):
    if str.isdigit(digit_str) or digit_str==".":
        return True

def get_num(num):
    if isinstance(num,int) or isinstance(num,float):
        return str
    number = "".join(list(filter(filter_num,str(num))))
    if "万" in num:
        return float(number)*10000
    else:
        return float(number)
    
    
if __name__=='__main__':
    print(get_num('剩余：49.67万'))