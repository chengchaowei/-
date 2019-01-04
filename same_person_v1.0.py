# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:17:23 2018

@author: Administrator
"""
from pathlib import Path
from  match_test import face_match_function
import random
from random import choice
import time
import os
import shutil


def return_count_frist(list_dirs_second):#返回统计次数以确定同一文件夹下是否是同一个人
    flag_index = 5
    i = 0
    while(flag_index):
        try:
            p_second = Path(list_dirs_second)#获取二级文件夹下的所有文件目录
            img_all_path = list(p_second.glob('**/*.jpg'))#定向查找jpg文件
            lens = len(img_all_path)
            img_frist_path = img_all_path[i]#获取jpg文件目录
            count = 0#设置计数器
            print("开始遍历单张图片")
            for img_choses_path in img_all_path[i+1:]:#遍历文件下所有图片
                time.sleep(0.4)
                
                score = face_match_function(img_frist_path,img_choses_path)#调用SDK函数接口实现比对，并返回得分
        #        print(score)
                if score == -1:
                    os.remove(img_choses_path)
                    continue
                if (score != None):                    
                    if score > 60.0:
                        count += 1
            print("遍历结束")
            if count > lens/2:
                print("确定将第一张照片作为基准照片")
                p_second_obj = Path(list_dirs_second)#获取二级文件夹下的所有文件目录
                img_all_path_obj = list(p_second_obj.glob('**/*.jpg'))#定向查找jpg文件
                for img_choses_path in img_all_path_obj:
                    time.sleep(0.4)
                    score = face_match_function(img_frist_path,img_choses_path)
                    if score < 60.0:
                        os.remove(img_choses_path)
                flag_index = 0
            elif count <= lens/2:
                print("第一张照片不是基准照片，删除")
                os.remove(img_frist_path)
                flag_index -= 1
        except IndexError:
               flag_index = 0
#    print(count) 

def screening_of_file_frist():#初次筛选，保证同一个文件夹下的都是同一个人
#    p = Path('D:/111111111111111111_test')
    p = Path('D:/111111111111111111_test')
    print("开始筛选单个文件夹")
    list_dir_frist =  [x for x in p.iterdir() if x.is_dir()]#获取一级文件夹list
    for list_dirs_frist in list_dir_frist:#遍历一级文件夹
        p_frist = Path(list_dirs_frist)#获取一级子文件夹下的文件夹目录
        list_dir_second = [x for x in p_frist.iterdir() if x.is_dir()]  #获取二级文件夹
        for list_dirs_second in list_dir_second: #遍历二级文件夹 
            print("开始遍历",list_dirs_second,"文件夹")
            if list_dir_second == None:
                continue
            return_count_frist(list_dirs_second)
    print("单个文件夹清理结束，确认每个文件夹下至有一个人===========")


def return_count_second(list_dir_second):
    flag_index = 5
    i = 0
    while(flag_index):
        try: 
            p_second_test1 = list_dir_second[i]           
            img_path_test1 = list(p_second_test1.glob('**/*.jpg'))
            same = 0
            for list_dirs_second in list_dir_second[i+1:]:
                print("开始遍历")
                p_second_test2 = Path(list_dirs_second)#获取二级文件夹下的所有文件目录
                img_path_test2 = list(p_second_test2.glob('**/*.jpg'))#定向查找jpg文件
                flag = 12
                count = 0          
                while(flag):
                    time.sleep(0.4)
                    score = face_match_function(choice(img_path_test1),choice(img_path_test2))
                    print(score)
                    if score >= 60.0:
                        count += 1
                    flag -= 1
                if count >= 2:
                    same += 1
            print("遍历结束")
            if same >= len(list_dir_second)/2:#将此文件夹作为标准，进行匹配
                for list_dirs_second in list_dir_second[i+1:]:
        #            print(list_dirs_second)
                    p_second_test2 = Path(list_dirs_second)#获取二级文件夹下的所有文件目录
                    img_path_test2 = list(p_second_test2.glob('**/*.jpg'))#定向查找jpg文件 
                    time.sleep(0.3)
                    score = face_match_function(choice(img_path_test1),choice(img_path_test2))
                    if score < 60.0:
                        list_dirs_second_str = str(list_dirs_second)
                        list_dirs_second_str.replace('\\','/')
                        print("已经确认将第一个文件夹作为基准文件夹，开始遍历其他文件夹",list_dirs_second_str)
                        shutil.move(list_dirs_second_str,'D:/diff_test/')
                flag_index = 0
                print("将第一个文件夹作为基准文件夹后筛选结束")
            else:
               p_second_test1_str = str(p_second_test1)
               p_second_test1_str.replace('\\','/')
               print("文件夹",p_second_test1_str,"不是基准文件，开始移动（剪切）到diff文件夹下",p_second_test1_str)
               shutil.move(p_second_test1_str,'D:/diff_test/')
               print("下一轮筛选开始")
               flag_index -= 1
               i += 1
        except IndexError:
               flag_index = 0
    
        
       
                
def screening_of_file_second():#二次筛选，对比不同文件夹下的人物是否是同一人
    p = Path('D:/111111111111111111_test')
    list_dir_frist =  [x for x in p.iterdir() if x.is_dir()]#获取一级文件夹list
    for list_dirs_frist in list_dir_frist:#遍历一级文件夹
        p_frist = Path(list_dirs_frist)#获取一级子文件夹下的文件夹目录
        list_dir_second = [x for x in p_frist.iterdir() if x.is_dir()]  #获取二级文件夹
        print(list_dir_second)        
        if len(list_dir_second) >= 2:         
            return_count_second(list_dir_second)
        p_flag_frist = Path(list_dirs_frist)
        list_flag_dir_second = [x for x in p_flag_frist.iterdir() if x.is_dir()]
        if len(list_flag_dir_second) != 0:  
            list_dirs_frist_str = str(list_dirs_frist)
            list_dirs_frist_str.replace('\\','/')
            print("最后总的二级目录开始剪切到same文件夹下",list_dirs_frist_str)
            shutil.move(list_dirs_frist_str,'D:/same_test/') 
            print("二级文件夹筛选完成")

            

if __name__ == "__main__":
    print("开始清洗单个文件夹============================================================")
    screening_of_file_frist()
    print("开始清理二级目录文件夹========================================================")
    screening_of_file_second()
    print("清洗成功=====================================================================")
#    img = screening_of_file_frist()
#    print(img)    
#    result = face_match_function(img[0],img[1])
#    print(result)    
#    path="D:/diff"
#    for i in os.walk(path):
#        print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    