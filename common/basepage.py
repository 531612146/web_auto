#-*-coding: UTF-8 -*-
'''
Created on 2019年12月9日
@author: LIJY
'''

from selenium.webdriver.remote.webdriver import WebDriver
import time
from futurn_loan.common.mylogging import mylogging
from futurn_loan.common.basepath import screenshot_path
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
from selenium.webdriver.common.action_chains import ActionChains




class BasePage():

    def __init__(self,driver:WebDriver):
        self.driver = driver
     
     # 等待元素可见   
    def wait_until_visible(self,ele_loc,img_doc,timeout = 10,poll_fre=0.5):
        mylogging.info("等待{}元素出现...",img_doc)
        start_time = time.time()
        try:            
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_any_elements_located, ele_loc)
        except:
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("等待{}元素可见，耗时{}...".format(img_doc,dur_time))
            
    # 查询元素是否存在   
    def wait_until_exist(self,ele_loc,img_doc,timeout = 10,poll_fre=0.5):
        mylogging.info("等待{}元素出现...",img_doc)
        start_time = time.time()
        try:            
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.presence_of_element_located, ele_loc)
        except:
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("等待{}元素存在，耗时{}...".format(img_doc,dur_time))
            
    def get_ele(self,ele_loc,img_doc):
        mylogging.info("获取元素{}开始...".format(img_doc))
        start_time = time.time()
        try:
            ele = self.driver.find_element(*ele_loc)
        except:
            # 获取失败，写日志，截图，抛出异常
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            # 获取成功，记录时间，记录日志，返回元素
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("获取{}元素，耗时{}...".format(img_doc,dur_time))            
            return ele
        
    def input_text(self,ele_loc,text,img_doc):
        mylogging.info("{}输入文字{}开始...".format(img_doc,text))
        start_time = time.time()
        # 等待元素可见，获取元素
        self.wait_until_visible(ele_loc, img_doc)
        ele = self.get_ele(ele_loc, img_doc)
        try:
            ele.send_keys(text)
        except:
            # 获取失败，写日志，截图，抛出异常
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("获取{}元素，耗时{}...".format(img_doc,dur_time))            
                           
    def ele_click(self,ele_loc,img_doc):
        mylogging.info("点击元素{}开始...".format(img_doc))
        start_time = time.time()
        # 等待元素可见，获取元素
        self.wait_until_visible(ele_loc, img_doc)
        ele = self.get_ele(ele_loc, img_doc)
        try:
            ele.click()
        except:
            # 获取失败，写日志，截图，抛出异常
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("点击{}元素，耗时{}...".format(img_doc,dur_time))
            
            
    def get_text(self,ele_loc,img_doc):
        mylogging.info("获取{}元素txt开始...".format(img_doc))
        start_time = time.time()
        # 等待元素可见，获取元素
        self.wait_until_visible(ele_loc, img_doc)
        ele = self.get_ele(ele_loc, img_doc)
        try:
            text = ele.text
        except:
            # 获取失败，写日志，截图，抛出异常
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("获取{}元素text，耗时{}...".format(img_doc,dur_time))
            return text
        
    # 获取元素的属性值    
    def get_attr(self,ele_loc,attr,img_doc):
        mylogging.info("获取{}元素{}参数开始...".format(img_doc,attr))
        start_time = time.time()
        self.wait_until_exist(ele_loc, img_doc)
        ele = self.get_ele(ele_loc, img_doc)
        try:
            attr = ele.get_attribute(attr)
        except:
            # 获取失败，写日志，截图，抛出异常
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("获取{}元素值为{}耗时{}...".format(img_doc,attr,dur_time))
            return attr
        
    def is_btn_enabled(self,ele_loc,img_doc):
        # 返回按钮是否可用
        mylogging.info("判断元素{}是否可用开始...".format(img_doc))
        start_time = time.time()
        self.wait_until_exist(ele_loc, img_doc)
        ele = self.get_ele(ele_loc, img_doc)
        return ele.is_enabled()
    
    # 鼠标悬浮
    def mouse_on(self,ele_loc,img_doc):
        mylogging.info("鼠标悬浮{}开始...".format(img_doc))
        start_time = time.time()
        self.wait_until_exist(ele_loc, img_doc)
        ele = self.get_ele(ele_loc, img_doc)
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            # 获取失败，写日志，截图，抛出异常
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("鼠标悬浮{}元素text，耗时{}...".format(img_doc,dur_time))
            

    # 鼠标悬浮
    def switch_to_iframe(self,ele_loc,img_doc):
        mylogging.info("切换iframe{}开始...".format(img_doc))
        start_time = time.time()
        self.wait_until_exist(ele_loc, img_doc)
        ele = self.get_ele(ele_loc, img_doc)
        try:
            self.driver.switch_to_frame(ele)
        except:
            # 获取失败，写日志，截图，抛出异常
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("切换iframe{}结束，耗时{}...".format(img_doc,dur_time))
            
    # 鼠标悬浮
    def set_attr(self,ele_loc,attr,value,img_doc,):
        mylogging.info("修改{}属性{}值为{}开始...".format(img_doc,attr,value))
        start_time = time.time()
        self.wait_until_exist(ele_loc, img_doc)
        ele = self.get_ele(ele_loc, img_doc)
        try:
            self.driver.execute_script('arguments[0].{}={}'.format(attr,value))
        except:
            # 获取失败，写日志，截图，抛出异常
            mylogging.error(traceback.format_exc())
            self.screenshot_save(img_doc)
            raise
        else:
            end_time = time.time()
            dur_time = end_time - start_time
            mylogging.info("修改{}属性{}值为{}结束，耗时{}...".format(img_doc,attr,value,dur_time))

    
    def screenshot_save(self,img_doc):
        # 保存截图传入名称拼接当前时间命名
        nowtime = time.strftime('%Y-%m-%d_%HH-%MM-%SS', time.localtime())
        img_name = img_doc + nowtime + ".png"
        # 拼接截图名称与截图保存路径
        img_file_path = os.path.join(screenshot_path,img_name) 
        try:
            mylogging.info("保存截图{}...".format(img_name))
            self.driver.save_screenshot(img_file_path)
        except:
            # 保存截图报错则写日志
            mylogging.exception("保存截图{}报错...".format(img_name))
            
    
        
        
        