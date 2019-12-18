#-*-coding: UTF-8 -*-
'''
Created on 2019年12月9日
@author: LIJY
'''
#-*-coding: UTF-8 -*-
'''
Created on 2019年9月26日
@author: LIJY
'''
import logging
from logging import Logger
from common import read_cfg
import os
from common import basepath
import time



class MyLogging(Logger):
    def __init__(self,name="autotest",logname="log.txt",level = 0,section="logger"):
        super().__init__(name,level)  # 父类初始化
        
        # 每天产生一个日志文件，获取当前的日期,与传入的logname组装成日志文件名称
        today = time.strftime('%Y-%m-%d', time.localtime())
        log_filename = today + "_" + logname        
        self.logfile = os.path.join(basepath.log_path,log_filename)
        # 如果今天的文件还没有创建，则新建文件，有则直接使用
        if not os.path.exists(self.logfile):
            f = open(self.logfile, 'w')
            f.close()
            
        # 读取配置文件中关于日志的配置
        ini_rd = read_cfg.IniRead()
        
         
        # 新建filehandler:
        if ini_rd.get_section_option(section, "file_logger_on"):    # 如果有设置filehandler则新建，添加到logger中
            file_handler = logging.FileHandler(self.logfile,encoding ='utf-8')
            file_handler.setLevel(int(ini_rd.get_section_option(section, "file_level")))
            file_fmt = logging.Formatter(ini_rd.get_section_option(section, "file_fmt"))
            file_handler.setFormatter(file_fmt)
            self.addHandler(file_handler)
            
        # 新建consolhandler
        if ini_rd.get_section_option(section, "consol_logger_on"):  # 如果设置有consolhandler则新建，添加到logger中
            consol_handler = logging.StreamHandler()
            consol_handler.setLevel(int(ini_rd.get_section_option(section, "consol_level")))
            consol_fmt = logging.Formatter(ini_rd.get_section_option(section, "consol_fmt"))
            consol_handler.setFormatter(file_fmt)
            self.addHandler(consol_handler)

mylogging = MyLogging()

if __name__=="__main__":
    logging1 = MyLogging()
    logging1.info("abcd1234")
    logging1.error("***8loggingerrortest****")
    logging1.debug("debug日志")
     
    
            
