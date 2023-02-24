#...............inrto..................#

'''
           image processing project
              Power_low and Logarithm Filter
                Ahmadali Jamali
                 02.15.2022
                  Teheran
                                    '''

#..............libraries...............#

import numpy as np
import math 
from skimage import io, img_as_float
import cv2
import random

#.............Functions................#

#transformation functions / power_low
def power_low(image):
    
    l = len(image)
    le = len(image[0])
    c = 1
    gamma = 0.8
    for i in range(l):
        for j in range(le):
    
            a = image[i][j]
            #power _ low gamma formula  
            image[i][j] = c*a**gamma 
                                         
    return np.array(image)

#transformation functions / log
def log(image):
    
    l = len(image)
    le = len(image[0])
    c = 1
    for i in range(l):
        for j in range(le):
    
            a = image[i][j]
            image[i][j] = c*math.log((a+1)) #log formula  
                                         
    return np.array(image)
    
#...............input..................#

#main function:
def main():

    #load image / gray and float 
    img = img_as_float(io.imread('wo.jpg',as_gray = True))

    #kernel
    kernel = np.ones((5,5),np.float32)/25
    gaussian_kernel = np.array([[1/16, 1/4, 1/16],
                                [1/8, 1/4,  1/8],
                                [1/16, 1/8, 1/16]])

    #orginal image:
    cv2.imshow('org',img)

    #power_low Image
    img2 = power_low(img)
    cv2.imshow('gamma',img2)

    #logarithm image
    im3 = log(img)
    cv2.imshow('log',im3)
   
    
    #output/showing
    cv2.waitkey()
    cv2.destruAllwindow()
    
#...............output.................#

#output/main function:    
if __name__ == "__main__":
    
    main()
                          
input()                            
