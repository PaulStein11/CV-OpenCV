
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Path of the PNG image to be loaded
imagePath =  "/home/paulstein/opencv/Example_course/PYHTON/ALPHA_PANTHER/panther.png"

# Read the image
# Note that we are passing flag = -1 while reading the image ( it will read the image as is)
imgPNG = cv2.imread(imagePath,-1)
print("image Dimension ={}".format(imgPNG.shape))
#First 3 channels will be combined to form BGR image
#Mask is the alpha channel of the original image
imgBGR = imgPNG[:,:,0:3]
imgMask = imgPNG[:,:,3]
plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(imgBGR[:,:,::-1]);plt.title('Color channels');
plt.subplot(122);plt.imshow(imgMask,cmap='gray');plt.title('Alpha channel');
plt.show()


