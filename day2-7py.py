# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:12:58 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    
    u = input("請輸入名子:")
    m = input("輸入訊息:")
    
    mc.postToChat("["+u+"]"+m)