# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:44:36 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
 
x,y,z = mc.player.getTilePos()
mc.setBlocks(x+50,y-1,z+50,x-50,y-1,z-50,438) 