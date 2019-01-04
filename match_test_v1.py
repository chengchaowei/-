 -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:32:20 2018

@author: Administrator
"""

from aip import AipFace
import numpy as np
import base64
import os
import cv2
from pathlib import Path
import random
from random import choice
import time
import os
import shutil
from PIL import Image
""" 你的 APPID AK SK """
APP_ID = '14640773'
API_KEY = '6TovD8BpXlRBceUpDGxL42KG'
SECRET_KEY = 'BUIztGzVz3MLrUNSbrpV98YhbE8ULif9'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
def face_match_function(img1,img2):    
    result = client.match([
        {
            'image': str(base64.b64encode(open(img1, 'rb').read()),'utf-8'),
            'image_type': 'BASE64',
        },
        {
            'image': str(base64.b64encode(open(img2, 'rb').read()),'utf-8'),
            'image_type': 'BASE64',
        }
    ])
    print(len(result))
    try:        
        i = 0
        for key in result:
            i+=1
            if (i == 6):
                for keys in result[key]:            
                    return result[key][keys]
    except TypeError:
        print("图片无法识别")
        return -1

def face_match_function(img1,img2):    
    result = client.match([
        {
            'image': str(base64.b64encode(open(img1, 'rb').read()),'utf-8'),
            'image_type': 'BASE64',
        },
        {
            'image': str(base64.b64encode(open(img2, 'rb').read()),'utf-8'),
            'image_type': 'BASE64',
        }
    ])

    return result

def feature_detect(image,image_path):
    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "landmark"
    options["max_face_num"] = 10
    options["face_type"] = "LIVE"
    im = Image.open(image_path)返回一个Image对象
    if (im.size[0]>500.0 or im.size[1]>500.0):        
        result = client.detect(image, imageType, options)
        face_num = result['result']['face_num']
        print(face_num)
        for i in range(0,face_num):
            print(result['result']['face_list'][i]['location'])
            location_left = int(result['result']['face_list'][i]['location']['left'])
            location_top = int(result['result']['face_list'][i]['location']['top'])
            location_width = int(result['result']['face_list'][i]['location']['width'])
            location_height = int(result['result']['face_list'][i]['location']['height'])
            image = cv2.imread(image_path)
            cropImg = image[location_top-50:(location_top+location_height),location_left-10:(location_left+location_width)+10]
            cv2.imwrite(image_path[:1]+str(i)+".jpg",cropImg)
    else:
        shutil.move(image_path,'D:/python_sfc/test')
if __name__ == "__main__":
    img1 = '4.jpg'
    image1 = str(base64.b64encode(open(img1, 'rb').read()),'utf-8')
    imageType = "BASE64"
    feature_image1 = feature_detect(image1,img1)
    feature_image2 = feature_detect(image2,img2)
    
    print(feature_image1)
    print(feature_image2)
    result = face_match_function(img1,img2)   
    path="D:/diff" 
    for i in os.walk(path):
        print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    