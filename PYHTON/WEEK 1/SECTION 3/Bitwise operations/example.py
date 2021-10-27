#Example


# Python program for blending of 
# images using OpenCV 
  
# import OpenCV file 
import cv2 
import numpy as np
#from dataPath import DATA_PATH
import matplotlib.pyplot as plt
#%matplotlib inline
import matplotlib
  
# Read Image1 
facePath = cv2.imread("/home/paulstein/opencv/Example_course/PYHTON/SECTION 3/Bitwise operations\musk.jpg") 
  
# Read image2 
glassPath = cv2.imread('/home/paulstein/opencv/Example_course/PYHTON/SECTION 3/Bitwise operations\sunglass.png', -1) 
facePath = np.float32(facePath)/255
glassPath = np.float32(glassPath)/255
# Blending the images with 0.3 and 0.7 
img = cv2.addWeighted(glassPath, 0.3, facePath, 0.7, 1) 
  
# Show the image 
cv2.imshow('image', img) 
  
# Wait for a key 
cv2.waitKey(0) 
  
# Distroy all the window open 
cv2.distroyAllWindows() 

