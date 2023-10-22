
"""
进行python 类的一些练习 
"""
from time import time,localtime,sleep
from abc import ABCMeta,abstractmethod
from MyDecorator import logger,timer
import os

class Clock:
    """数字时钟"""
    def __init__(self,hour=0,minute=0,second=0):
        """
        构造函数
        param hour   小时
        param minute 分钟
        param second 秒
        """
        self.hour = hour
        self.minute = minute
        self.second= second
        self._milisec = 100
    
    def run(self):
        """
        时钟运行
        """
        sleep(1)
        self.second +=1
        if self.second >=60:
            self.second=0
            self.minute+=1
            if self.minute >=60:
                self.hour+=1
                self.minute=0
                if self.hour>=24:
                    self.hour=0
        self.show()
                    
    def show(self):
        """
        显示时间
        """
        os.system("cls")
        print("{0}:{1}:{2}".format(self.hour,self.minute,self.second))
    
    def _milisec(self):
        print(self.__milisec)
    
    @logger
    @staticmethod
    def is_valid(hour,minute,secod):
        if hour>24 or minute>59 or second>59:
            return False
        return True
        
    @classmethod   
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

def test1():
    clock = Clock.now()
    print(Clock.is_valid(23,69,23))
    
    #while True:
    #    clock.run()
    
'''
类的继承练习
'''

class Employee(object,metaclass=ABCMeta):
    
    def __init__(self,name):
        self._name = name
        
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,name):
        self._name = name
    
    @abstractmethod
    def get_salary(self):
        pass
        
    def get_compony(self):
        print("来自三国演义有限公司")
    
        
class Manager(Employee):
    def __init__(self,name):
        super().__init__(name)
    
    @logger 
    @timer    
    def get_salary(self):
        print('Manager{}的工资是12000'.format(self._name))
        
    def __str__(self):
        return '我是:{}'.format(self._name)
        

class Programer(Employee):
    def __init__(self,name,hour=0):
        super().__init__(name)
        self._hour = hour
    
    @logger    
    @timer
    def get_salary(self):
        print('Programer {}的工资是{}'.format(self._name,150*self._hour))
        
    def __str__(self):
        return '我是:{}'.format(self._name)
        
def test2():
    listp =[Manager('刘备'),Manager('曹操'),Programer("张飞",100),Programer("吕布",70)]
    for p in listp:
        print(p)
        p.get_salary()
        p.get_compony()
    
    
    
if __name__ =="__main__":
   
    test2()
    
        
    
    

 
 
 
        
    







        
        
        