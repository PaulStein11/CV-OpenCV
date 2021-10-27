# Import libraries
import cv2
import numpy as np
#import matplotlib.pyplot as plt // Doesnt have to be included to show the matrix
#%matplotlib inline // only for Jupiter notebook

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

imagePath = "/home/paulstein/opencv/Example_course/PYHTON/ZERO IMAGE/number_zero.jpg"

# Read image in Grayscale format
testImage = cv2.imread(imagePath,0)
#selection of the matrix and change it for a new value // testImage[0, 0] = 200
test_roi = testImage[0:2, 0:4] = 200  #Adding the =200 it replace the value in that specific area

#print(testImage)

print("Original Matrix\n{}\n".format(testImage))
print("Selected Region\n{}\n".format(test_roi))
print("Data type = {}\n".format(testImage.dtype))
print("Object type = {}\n".format(type(testImage)))
print("Image Dimensions = {}\n".format(testImage.shape))



