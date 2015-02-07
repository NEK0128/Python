#!/usr/bin/python
# -*- encoding:utf-8 -*-  

from PIL import Image
import os
import sys

splitWidthNum = 9.0
splitHeightNum = 5.0

def Split(im):
    width,height = im.size
    w1, h1 = 0,0
    buff = []

    print "w(%f),H(%f)"%(width, height)
    h = 0
    while h < splitHeightNum:
       h1 = height*(h/splitHeightNum)
       w = 0
       while w < splitWidthNum:
            w1 = width*(w/splitWidthNum)
            w2,h2 = (w1 + (width*(1/splitWidthNum))), (h1 + (height*(1/splitHeightNum)))
            print "crop (%f, %f, %f, %f)" % (w1, h1, w2, h2)
            c = im.crop((int(w1), int(h1), int(w2), int(h2)))
            buff.append(c)
            w += 1
       h += 1
    return buff


if __name__=='__main__':
    im = Image.open(sys.argv[1])
    num = 1
    for ig in Split(im):
        ig.save("result/%d.png"%num, "PNG")
        num += 1
