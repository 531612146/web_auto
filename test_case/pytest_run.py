#-*-coding: UTF-8 -*-
'''
Created on 2019年12月11日
@author: LIJY
'''

#-*-coding: UTF-8 -*-
'''
Created on 2019年12月11日
@author: LIJY
'''

import pytest
import os
import time
from common import basepath


# 跑案例
if __name__=='__main__':
    # 生成报告文件名    
    detail_time = time.strftime('%Y-%m-%d_%HH-%MM-%SS', time.localtime())
    report_file = os.path.join(basepath.report_path,detail_time+'.html')    
    
    # 开始跑南里，失败重试两次，输出到html报告
    pytest.main(['-m','smoke','.'+os.sep+'test_bid.py',
                 "--reruns","2",
                 "--html={}".format(report_file),
                 "--alluredir={}".format(basepath.allure_path)]
                )




