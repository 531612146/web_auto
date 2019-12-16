#-*-coding: UTF-8 -*-
'''
Created on 2019年12月11日
@author: LIJY
'''

import pytest
import os
import time
from futurn_loan.common.basepath import report_path



# 跑案例
if __name__=='__main__':
    # 生成报告文件名
    detail_time = time.strftime('%Y-%m-%d_%HH-%MM-%SS', time.localtime())
    report_file = os.path.join(report_path,detail_time+'.html')
    pytest.main(['-m','smoke','.'+os.sep+'test_bid.py',"--reruns","2","--html={}".format(report_file)])