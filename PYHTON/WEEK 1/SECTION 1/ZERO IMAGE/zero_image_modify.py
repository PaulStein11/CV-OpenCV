import numpy as np
import cv2
from matplotlib import pyplot as plt


imagePath = "/home/paulstein/opencv/Example_course/PYHTON/ZERO IMAGE/number_zero.jpg"
testImage = cv2.imread(imagePath,1)
#plt.imshow(testImage) // Shows the image in its actual size


#plt.figure(figsize=[20,20])  //Changes size of the image


#testImage[0, 0] = (0, 255, 255)
#plt.subplot(131);plt.imshow(testImage[:,:,::-1])
#testImage[1, 2] = (255, 255, 1)
#plt.subplot(132);plt.imshow(testImage[:,:,::-1])
#testImage[2, 2] = (255, 0, 255)
#plt.subplot(133);plt.imshow(testImage[:,:,::-1])


testImage[0:3,0:3] = (255,0,0)
testImage[3:6,0:3] = (0,255,0)
testImage[6:9,0:3] = (0,0,255)

plt.imshow(testImage[:,:,::-1])
plt.show()

