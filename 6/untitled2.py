# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:46:29 2022

@author: Федя
"""
from PIL import Image
frames = 24
images = [Image.open(f"filename{n}.png") for n in range(frames)]

images[0].save('ball2.gif', save_all=True, append_images=images[1:], duration=100, loop=0)