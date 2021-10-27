# Import libraries
import cv2
import numpy as np
#import matplotlib.pyplot as plt 
#%matplotlib inline // only for Jupiter notebook

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

imagePath = "/home/paulstein/opencv/Example_course/PYHTON/Boy Image/boy.jpg"

testImage = cv2.imread(imagePath,0)


# Read an image
boy = cv2.imread(imagePath)
# Display the image using imshow
cv2.imshow("Boy", boy)
# Wait for user to press a key
cv2.waitKey(0)
# Destroy the window
cv2.destroyAllWindows()





