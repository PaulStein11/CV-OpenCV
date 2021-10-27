# Import libraries
import cv2
import numpy as np
#from dataPath import DATA_PATH
import matplotlib.pyplot as plt 	 	

import matplotlib

#Read image
image = cv2.imread("/home/paulstein/opencv/Example_course/PYHTON/SECTION 2/Boy_image_modify/boy.jpg")

# Let's see what image we are dealing with
plt.imshow(image[:,:,::-1])

# Crop out a rectangle
# x coordinates = 170 to 320
# y coordinates = 40 to 200
#crop = image[40:200,170:320]
#plt.imshow(crop[:,:,::-1])
# -----------------------------------------------------------

##Create a copy from the original
#copiedImage = image.copy()
#plt.imshow(copiedImage[...,::-1])
# ///// CROPPING AND PASTING
#copyRoi = image[40:200,180:320]
# Find height and width of the ROI
#roiHeight,roiWidth = copyRoi.shape[:2]
# Copy to left of Face
#copiedImage[40:40+roiHeight, 10:10+roiWidth] = copyRoi
# Copy to right of Face
#copiedImage[40:40+roiHeight, 330:330+roiWidth] = copyRoi
# Display the output
#plt.figure(figsize=[15,15])
#plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("Original Image");
#plt.subplot(122);plt.imshow(copiedImage[...,::-1]);plt.title("Output Image");

# --------------------------------------------------------

# Set rows and columns
#resizeDownWidth = 300
#resizeDownHeight = 200
#resizedDown = cv2.resize(image, (resizeDownWidth, resizeDownHeight), interpolation= cv2.INTER_LINEAR)

# Mess up with the aspect ratio
#resizeUpWidth = 600
#resizeUpHeight = 900
#resizedUp = cv2.resize(image, (resizeUpWidth, resizeUpHeight), interpolation= cv2.INTER_LINEAR)

#plt.figure(figsize=[15,15])
#plt.subplot(131);plt.imshow(image[:,:,::-1]);plt.title("Original Image")
#plt.subplot(132);plt.imshow(resizedUp[:,:,::-1]);plt.title("Scaled Up Image")
#plt.subplot(133);plt.imshow(resizedDown[:,:,::-1]);plt.title("Scaled Down Image")
# -----------------------------------------------------------------
# Scaling Down the image 1.5 times by specifying both scaling factors
scaleUpX = 1.5
scaleUpY = 1.5

# Scaling Down the image 0.6 times specifying a single scale factor.
scaleDown = 0.6

scaledDown = cv2.resize(image, None, fx= scaleDown, fy= scaleDown, interpolation= cv2.INTER_LINEAR)

scaledUp = cv2.resize(image, None, fx= scaleUpX, fy= scaleUpY, interpolation= cv2.INTER_LINEAR)

plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(scaledDown[...,::-1]);plt.title("Scaled Down Image, size = {}".format(scaledDown.shape[:2]));
plt.subplot(122);plt.imshow(scaledUp[...,::-1]);plt.title("Scaled Up Image, size = {}".format(scaledUp.shape[:2]));
plt.show()


