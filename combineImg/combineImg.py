#!/usr/bin/python
# -*- encoding:utf-8 -*-  

from PIL import Image
import os
import sys

num = 3
newimg = Image.new("RGB", (624, 70), (255,255,255))
n = 0
a = ["1m", "2m", "5p"]
while n < num:
    img = Image.open("data/%s.png"%a[n], "r")
    newimg.paste(img, (n * 48, 0))
    n += 1


newimg.save("result/hai.png", "PNG")
