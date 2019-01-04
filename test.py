# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:16:26 2018

@author: Administrator
"""

#import shutil,os
#
#shutil.move('D:/1111/1186/6675','D:/diff_test')


#import os, sys,random
#from pathlib import Path
#import random
#from random import choice
#import time
#import shutil
 

## Path to be created
#time.localtime(time.time())
#
#number = random.randint(10000,50000)
#
#path = 'D:/new_kof/same/'+str(number)
# 
#
#os.mkdir(path, 493 ) #decimal equivalent of 0755 used on Windows
#
# 
#
#print ("Path is created")


#p = Path('D:/new_kof/111111111111111111')
##img_path_test1 = list(p.glob('**/*.jpg'))
#list_dir_frist =  [x for x in p.iterdir() if x.is_dir()]
#for list_dirs_frist in list_dir_frist:
#       p_frist = Path(list_dirs_frist)#获取一级子文件夹下的文件夹目录
#       list_dir_second = [x for x in p_frist.iterdir() if x.is_dir()]  #获取二级文件夹  
#       print(list_dir_second[0])
#       list_move = str(list_dir_second[0])
#       print(list_move[35:])
       
#list_dir_frist =  [x for x in p.iterdir() if x.is_dir()]
#for list_dirs_frist in list_dir_frist:
#    list_test = str(list_dirs_frist)
#    print(list_test[7:11])

#删除文件



#dirPath = "D:/face/face_test/img1/20180702/"
#list_file = Path(dirPath)
#img_path_test2 = list(list_file.glob('*.jpg'))
#for list_file_move in img_path_test2:
#    list_move = str(list_file_move)
#    list_move = list_move.replace('\\','/')
#    os.remove(list_move)
#
#print ('删除成功')



#import os
#filepath = "D:/face/fileUpload_result"  # 文件夹路径
#delect = "data"   # 要删除的名字字符串
#if __name__ == "__main__":
#    if not os.path.exists(filepath):
#        print("目录不存在!!")
#        os._exit(1)
#    filenames = os.listdir(filepath)
#    print("文件数目为%i" %len(filenames))
#    count = 0
#    for name in filenames:
#        os.rename(filepath + '/' + name, filepath + '/' + str(count))
#        count += 1
#        if count % 100 == 0:
#            print("第%i个文件已经改名完成" %count)













