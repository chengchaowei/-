# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:47:26 2018

@author: Administrator
"""

from pathlib import Path
from  match_test_v1 import face_match_function
import random
from random import choice
import time
import os
import shutil



#def sample_found_function_frist(list_dirs_frist):
#    lens = len()
#    p_dir_second = Path(p_dirs_frist)
#    img_path_test = list(p_dir_second.glob('**/*.jpg'))
    
    

def sample_found_function(list_dir_frist):
    p_frist = Path(list_dir_frist)
    p_dir_frist = [x for x in p_frist.iterdir() if x.is_dir()]#找出总的文件夹下的所有问价目录
    lens = len(p_dir_frist)
    i = 1
    for p_dirs_frist in p_dir_frist:
        p_dir_second = Path(p_dirs_frist)
        img_path_test = list(p_dir_second.glob('**/*.jpg'))
        for p_dirs_test in p_dir_frist[i:]:
            img_path_test_sample = list(p_dirs_test.glob('**/*.jpg'))
            try:
                time.sleep(0.4)
                score = face_match_function(choice(img_path_test),choice(img_path_test_sample))
                if score > 60.0:
                    print(p_dirs_frist,"和",p_dirs_test,"是同一个人")
            except TypeError:
                print(p_dirs_test,"文件夹图片太大")
        print("第 ",i," 个文件夹遍历结束，开始下一轮")
        i += 1




if __name__ == "__main__":
    path = "D:/face/fileUpload_result/"
    sample_found_function(path)






















