# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:31:21 2018

@author: Administrator
"""

from pathlib import Path
from  match_test_v1 import face_match_function
import random
from random import choice
import time
import os
import shutil



def kinds_of_comparison(list_dir_second):
    flag_index = 1
    i = 0
    delet1 = 0
    delet2 = 0
    while(flag_index):
        try: 
            p_second_test1 = list_dir_second[i] 
            list_mkdir_new = str(p_second_test1)
            print(list_mkdir_new[35:])#获取文件夹的名称
            path = 'D:/new_kof/same/'+list_mkdir_new[35:]#新建文件夹
            os.mkdir(path,493)               
            img_path_test1 = list(p_second_test1.glob('**/*.jpg'))
            if len(img_path_test1) == 0:
                  delet1 = 1              
            same = 0
            for list_dirs_second in list_dir_second[i+1:]:
                print("开始遍历")
                p_second_test2 = Path(list_dirs_second)#获取二级文件夹下的所有文件目录
                img_path_test2 = list(p_second_test2.glob('**/*.jpg'))#定向查找jpg文件
                if len(img_path_test2):
                    delet2 = 1
                flag = 12
                count = 0          
                while(flag):
                    time.sleep(0.4)
                    score = face_match_function(choice(img_path_test1),choice(img_path_test2))
                    print(score)
                    if score >= 60.0:
                        count += 1
                    flag -= 1
                    if score == -1:
                        flag += 1
                if count >= 5:
                    list_move = str(p_second_test2)
                    list_move = list_move.replace('\\','/')
                    shutil.move(list_move,path)
            list_move = list_mkdir_new.replace('\\','/')
            shutil.move(list_move,path)
            flag_index = 0
            print("遍历结束")
        except IndexError:
            if delet1 == 0:
                list_move = list_mkdir_new.replace('\\','/')
                os.removedirs(list_move)
            if delet2 == 0:
                list_move = str(p_second_test2)
                list_move = list_move.replace('\\','/')
                os.removedirs(list_move)
            flag_index = 0
    
        
       
                
def adress_to():#二次筛选，对比不同文件夹下的人物是否是同一人
    p = Path('D:/new_kof/111111111111111111')
    list_dir_frist =  [x for x in p.iterdir() if x.is_dir()]#获取一级文件夹list
    for list_dirs_frist in list_dir_frist:#遍历一级文件夹
        print("开始遍历",list_dirs_frist,"=====================================")
        flag = 1
        while(flag): 
            p_frist = Path(list_dirs_frist)#获取一级子文件夹下的文件夹目录
            list_dir_second = [x for x in p_frist.iterdir() if x.is_dir()]  #获取二级文件夹  
            print("文件夹",p_frist,"开始清理")
            if len(list_dir_second) >= 2:
                kinds_of_comparison(list_dir_second)
            elif len(list_dir_second) == 1:
                list_dirs_frist_str = str(list_dirs_frist)                
                list_dirs_frist_str.replace('\\','/')
                print("最后总的二级目录开始剪切到same文件夹下",list_dirs_frist_str)
                shutil.move(list_dirs_frist_str,'D:/new_kof/same/') 
                print("二级文件夹筛选完成")
                flag = 0
            elif len(list_dir_second) == 0 :
                flag = 0
            
if __name__ == "__main__":
    adress_to() 
    print("====================================类类之间清洗完成=================")    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            