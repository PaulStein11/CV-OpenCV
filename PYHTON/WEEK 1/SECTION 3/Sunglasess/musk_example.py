# EXAMPLE OF ELON MUSK DIFFERENT OPTIONS

import cv2
import numpy as np
import matplotlib.pyplot as plt 	 	
import matplotlib

# Read image
faceImagePath ="/home/paulstein/opencv/Example_course/PYHTON/SECTION 3/Sunglasess/musk.jpg"
faceImage = cv2.imread(faceImagePath)
glassesImagePath = "/home/paulstein/opencv/Example_course/PYHTON/SECTION 3/Sunglasess/sunglass.png"
glassImage = cv2.imread(glassesImagePath, -1)

#print("Original Image Datatype : {}".format(faceImage.dtype))
#print("Original Image Datatype : {}".format(glassImage.dtype))

#It is a good practice to convert the uint8 to float and normalize the range to [0,1] and change it back to [0,255] after doing all arithmetic operations
faceImage = np.float32(faceImage)/255
print("Actual Image Datatype : {}".format(faceImage.dtype))
glassImage = np.float32(glassImage)/255
print("Actual Image Datatype : {}".format(glassImage.dtype))

# Resize the image to fit over the eye region
glassImage = cv2.resize(glassImage, None, fx=0.5, fy=0.5)
glassHeight, glassWidth, nChannels = glassImage.shape
print("Sunglass dimension ={}".format(glassImage.shape))

# Separate the Color and alpha channels
glassBGR = glassImage[:,:,0:3]
glassMask1 = glassImage[:,:, 3]

## --- REPLACE THE SELECTED REGION OF THE EYES TO THE PNG GLASSES
# Top left corner of the glasses
topLeftRow = 130
topLeftCol = 130

bottomRightRow = topLeftRow + glassHeight
bottomRightCol = topLeftCol + glassWidth

# Since Face Image is a 3-channel image, we create a 3 channel image for the mask
glassMask = cv2.merge(( glassMask1, glassMask1, glassMask1))

# Make a copy
faceWithGlassesArithmetic = faceImage.copy()
# Get the eye region from the face image
eyeROI= faceWithGlassesArithmetic[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]
# Use the mask to create the masked eye region
maskedEye = cv2.multiply(eyeROI,(1  - glassMask ))
# Use the mask to create the masked sunglass region
maskedGlass = cv2.multiply(glassBGR, glassMask)
# Combine the Sunglass in the Eye Region to get the augmented image
eyeRoiFinal = cv2.add(maskedEye, maskedGlass)

# Display the intermediate results
plt.figure(figsize=[20,20])
plt.subplot(131);plt.imshow(maskedEye[...,::-1]);plt.title("Masked Eye Region")
plt.subplot(132);plt.imshow(maskedGlass[...,::-1]);plt.title("Masked Sunglass Region")
plt.subplot(133);plt.imshow(eyeRoiFinal[...,::-1]);plt.title("Augmented Eye and Sunglass")

# Replace the eye ROI with the output from the previous section
faceWithGlassesArithmetic[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]= eyeRoiFinal
# Display the final result
plt.figure(figsize=[20,20]);
plt.subplot(121);plt.imshow(faceImage[:,:,::-1]); plt.title("Original Image");
plt.subplot(122);plt.imshow(faceWithGlassesArithmetic[:,:,::-1]);plt.title("With Sunglasses");
plt.show()


