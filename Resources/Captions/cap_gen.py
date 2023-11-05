#!/usr/bin/python3
# coding: utf-8
import sys
print(sys.getdefaultencoding())
import glob
#import cv2
import unicodedata
import os
import csv


os.chdir(os.path.dirname(os.path.abspath(__file__)))
images = glob.glob("./images/**", recursive=True)
# print(images)
for cand in images:
    if cand.split(".")[-1] in ["png", "jpg", "gif", "JPG", "PNG"]:
        path = cand.replace('\\', '/')
        path = path.replace('./', '/')
        
        name = cand.split(".")[-2].split("\\")[-1]
        content = "#title=" + name + "\n" + "#path=" + path
        
        print(name)
        print(content)
        
        print(os.getcwd() + "/" + name + ".txt")
        with open(os.getcwd() + "/" + name + ".txt", "w") as f:
            f.write(content)

