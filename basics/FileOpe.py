

#  能够读写多语言文本的方法  读写[] dict() 对象到文本
# 读写CSV 和读写Excel
# 输出到指定路径
#读取D:\chaiz\OpenSource\FreeCAD19\code下所有文件，病统计每个文件代码行数，讲文件名称输出，

# 读取不同编码的txt文件，并输出
import os
import pandas as pd
import time
import json
import csv
from MyDecorator import logger

def readTxt(fileName,iencoding):
    try:
        with open(fileName,mode='r+',encoding=iencoding) as f:
            cont = f.read()
            print(cont)
            f.close()
            return cont            
    except Exception as e:
        print(e.args)
    finally:
        print('读取成功')
        
def readTxt2(fileName,iencoding):
    try:
        with open(fileName,mode='r+',encoding=iencoding) as f:
            #print(type(f))
            lines = f.readlines()            
            #for line in lines:
            #    print(line)
            f.close()
            return lines
    except Exception as e:
        print(e.args)
    finally:
        print('读取成功')
        
        
def writeTxt(filePath,mode,content):
    with open(filePath,mode = mode) as f: 
        if mode in ['a','a+']:
            f.write("\r\n")
        if  isinstance(content,str):
            f.write(content)
        elif isinstance(content,list):
            for line in content:
                f.write(line)
        elif isinstance(content,dict):
            for item in content.items():#每个item是一个tuple（key，value）
                f.write(":".join( [ str(item[0]),str(item[1]) ] ) +"\n") 
                #f.write("\n") 
        f.close()
        
@logger
def parseDir(path):
    listFiles = []
    for root,dirs,files in os.walk(path,topdown=False):
        for file in files:
            listFiles.append(os.path.join(root,file))
    return listFiles
"""
将D:\chaiz\OpenSource\FreeCAD\FreeCAD_code目录下所有文件名输出到 FreeCAD.txt中
统计所有文件类型， 以及该类型对应的文件个数
"""




def writeJson():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('datastr.json', 'w', encoding='utf-8') as fs:
            #json.dump(mydict, fs)
            jstr = json.dumps(mydict)
            fs.write(jstr)
            
    except IOError as e:
        print(e)
    print('保存数据完成!')

def readJson():
    try:
        with open('datastr.json', 'r', encoding='utf-8') as fs:
            #json.dump(mydict, fs)
            cont = fs.read()
            jstr = json.loads(cont)
            for key,value in jstr.items():
                print(key)
                print(value)
            
    except IOError as e:
        print(e)
    print('保存数据完成!')

def writeCSV(filename):
    try:
        with open(filename,mode="w+",encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['骆昊', 38, '叫兽'])
            writer.writerow(['狄仁杰', 25, '砖家'])
    except Exception as ep:
        print(ep)
    finally:
        if(f):
            f.close()
            
    
            
    


@logger
def task1():
    listFiles = parseDir(r"D:\chaiz\OpenSource\FreeCAD\FreeCAD_code")
    extDic= dict()
    for file in listFiles:    
        ext = os.path.splitext(file)[-1].strip('.')
        #print(ext)
        if  ext not in extDic.keys():
            extDic[ext]=[]
        extDic[ext].append(file)
    outputname = time.strftime('%y-%m-%y %H_%M_%S.txt',time.localtime())    
    with open(outputname,mode='a+') as f:
        for key,files in extDic.items():
            tmp = key+"后缀文件有{0}个\n".format(len(files))
            f.write(tmp)
            for filename in files:
                tmp= "\t"+filename+"\n"
                f.write(tmp)
        f.close()
        
        

def task2():
    listFiles = parseDir(r"D:\chaiz\OpenSource\FreeCAD\FreeCAD_code")
    extDic= dict()
    for file in listFiles:    
        ext = os.path.splitext(file)[-1].strip('.')       
        if  ext not in extDic.keys():
            extDic[ext]=[]
        extDic[ext].append(file)
        
    df = pd.DataFrame(listFiles)
    df.to_excel("FreeCAD.xlsx")

if __name__ == '__main__':
    #testReadJson()
    writeCSV("csvtest.csv")
    
    

 
 
 
        
    







        
        
        