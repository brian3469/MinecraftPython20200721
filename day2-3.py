# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:42:49 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z = mc.player.getTilePos()

height = 100
lenght = 100
width = 100

mc.setBlocks(x,y,z,x+height,y+lenght,z+width,2)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+lenght-1,0)