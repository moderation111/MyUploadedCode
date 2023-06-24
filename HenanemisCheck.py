
import numpy as np
import pandas as pd
import multiprocessing as mp
import os

def is_chinese(char):
    if '\u4e00' <= '\u9fff':
        return True
    else: 
        return False

def Ch_trans_to_En(string):
    E_pun = u',.!?[]()"\''
    C_pun = u'，。！？【】（）“‘'
    table = {ord(f):ord(t) for f,t in zip(C_pun,E_pun)}
    return string.translate(table)

def removeChnAndCharacter(str1):
    C_pun = u'，。！？【】（）“‘'
    strTmp = ''

    if not isinstance(str1,str):
        return strTmp

    for i in range(len(str1)):
        if str1[i] >= u'\u4e00' and str1[i] <= u'\u9fa5' \
                or str1[i] >= u'\u3300' and str1[i] <= u'\u33FF' \
                or str1[i] >= u'\u3200' and str1[i] <= u'\u32FF' \
                or str1[i] >= u'\u2700' and str1[i] <= u'\u27BF' \
                or str1[i] >= u'\u2600' and str1[i] <= u'\u26FF' \
                or str1[i] >= u'\uFE10' and str1[i] <= u'\uFE1F' \
                or str1[i] >= u'\u2E80' and str1[i] <= u'\u2EFF' \
                or str1[i] >= u'\u3000' and str1[i] <= u'\u303F' \
                or str1[i] >= u'\u31C0' and str1[i] <= u'\u31EF' \
                or str1[i] >= u'\u2FF0' and str1[i] <= u'\u2FFF' \
                or str1[i] >= u'\u3100' and str1[i] <= u'\u312F' \
                or str1[i] >= u'\u21A0' and str1[i] <= u'\u31BF' \
                :
            pass
        else:
            if str1[i] in C_pun:
                st = Ch_trans_to_En(str1[i])
            else:
                st = str1[i]
            strTmp += st

    return strTmp

HenanEmisPath = 'E:\\UploadCodeFile\\Henan_emis\\Henan_emis\\'

monthlyEmisPath = HenanEmisPath + 'monthly_emis_2016\\'

if __name__=='__main__':
    print('HenanemisCheck.py')
    #读取检查标准
    
    #检查月排放文件
    #检查行业，

    sectornameList = ['POWER','DS','LN','KK']####testvalue

    tempCheckpath = monthlyEmisPath + 'emis_data\\'
    filelist = os.listdir(tempCheckpath)
    print(filelist)
    for i in sectornameList: 
        sign = 'Lack'
        for j in filelist:          
            if i+'.' in j:
                sign = 'Exist'
                print(i+' is in filelist')
                suffixname = j.split('.')[1]
                filereader = open(tempCheckpath+j,'r',encoding='utf-8')
                #filereader = open(tempCheckpath+j,'rb').read().decode(encoding='utf-8')

                #filereader.decode("utf-8")
                #检查文件中是否存在中文字符
                for line in filereader:
                    #print(line)
                    for item in line:
                        if item in '，。！？【】（）“‘':
                            print('file '+j+' has chinese character')
                            #filereader.close()                            
                            #exit()
                        elif item == ' ':       
                            print('file '+j+' has space')
                        elif item == 'NULL':
                            print('file '+j+' has NULL')
                        elif item == 'NAN':
                            print('file '+j+' has NAN')
                    print(line[-2])
                    print(type(line[-1]))
                    if isinstance(line[-2],str):

                        print('file '+j+' has no \\n') 


        if sign == 'Lack':
            print('lack of '+i+' file')
    
                # sectorlistinfile = filereader[0]
                # tt=removeChnAndCharacter(sectorlistinfile)
                # print(tt)
                #for line in filereader:
                    #print(line)
                #df = pd.read_csv(tempCheckpath+j)
                #print(df)



