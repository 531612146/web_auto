#-*-coding: UTF-8 -*-
'''
Created on 2019年12月3日
@author: LIJY
'''


from futurn_loan.common import HTMLTestRunner
import unittest
from datetime import datetime
import os

class RunReport:
    def __init__(self,casepath,pattern,reportname):
        '''
        初始化case路径，案例格式，报告地址
        '''
        self.reportname = reportname
        self.loader = unittest.TestLoader()
        self.suite = self.loader.discover(casepath, pattern)  # 初始化的时候就加载好测试案例
    
    def runcase(self):
        '''
        把跑案例方法封装到一个方法里面
        '''
        # 生成文件名
        # 把reportname加上时间戳
        time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.reportname = os.path.join(os.path.dirname(os.path.abspath(__file__)),(self.reportname+time))+'.html'
        
        with open(self.reportname,'wb') as f:
            runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2)
            runner.run(self.suite)
    
if __name__=='__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    case_path = os.path.join(base_path,"test_case")
    try:
        run1 = RunReport(case_path,'test*.py','loginrun')
    except Exception as e:
        print(e)
        
    try:
        run1.runcase()
    except Exception as e:
        print('******runcase报错了******',str(e))
