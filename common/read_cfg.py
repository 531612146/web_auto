#-*-coding: UTF-8 -*-
'''
Created on 2019年12月9日
@author: LIJY
'''


from configparser import ConfigParser
from common import basepath

 
class IniRead:
    # 我的带有中文的文件读取会有问题，默认用ANSI编码格式可以正常
    def __init__(self,filename=basepath.cfg_file,encoding='ANSI'):
        self.config = ConfigParser()
        self.config.read(filename,encoding)
 

    def get_section_option(self,section,option):  # 如果section或option不在就返回None
        try:
            return self.config.get(section,option)
        except:
            return None
    def get_section_options(self,section):
        return self.config.items(section)
        
     
class IniWrite:
    def __init__(self,filename,encoding = "ANSI"):
        '''
        读和写放在一个文件，默认用ANSI编码
        '''
        self.config = ConfigParser()
        self.config.read(filename, encoding)
        self.filename = filename
        self.encoding = encoding
        
    
    def add_section(self,*args):   
        # 传入可迭代对象，如果section不存在，那就新增,写完后自动保存文件
        for section in args:
            if section not in self.config.sections():
                self.config.add_section(section)
        with open (self.filename,"w",encoding=self.encoding) as f:
            self.config.write(f)
    
    def set_options(self,section,**kwargs):
        # 包装个设置一个section多个值的类，写完后自动保存文件
        options = kwargs
        for option in kwargs:
            self.config.set(section,option,options[option])
         
        with open (self.filename,"w",encoding=self.encoding) as f:
            self.config.write(f)
         

if __name__=='__main__':
    ini_rd = IniRead(basepath.cfg_file)
    print(ini_rd.get_section_option("logger", "file_logger_on"))
    print(ini_rd.get_section_options("logger"))
    
    