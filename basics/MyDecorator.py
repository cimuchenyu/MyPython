

'''
修饰器练习
添加一个计时器  添加一个
'''
import time

def logger(func):
    def wrapper(*args,**kw):
        print('{}开始执行'.format(func.__name__))
        result = func(*args,**kw)
        print('{}执行完毕'.format(func.__name__))
        return result
    return wrapper
    
    
def timer(func):
    def wrapper(*args,**kw):
        t1=time.time()
        result = func(*args,**kw)
        t2=time.time()
        print('{}执行时间是{}s'.format(func.__name__,t2-t1))
        return result
    return wrapper
        
    

    