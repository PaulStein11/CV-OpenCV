# Import libraries
import cv2
import numpy as np
#from dataPath import DATA_PATH
import matplotlib.pyplot as plt
#%matplotlib inline
import matplotlib

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
matplotlib.rcParams['image.interpolation'] = 'bilinear'

# Load the Face Image
faceImagePath = "/home/paulstein/opencv/Example_course/PYHTON/SECTION 3/Sunglasess/musk.jpg"
faceImage = cv2.imread(faceImagePath)
plt.imshow(faceImage[...,::-1]);plt.title("ELON MUSK")
# Make a copy
faceWithGlassesBitwise = faceImage.copy()

# Load the Sunglass image with Alpha channel
glassimagePath = "/home/paulstein/opencv/Example_course/PYHTON/SECTION 3/Sunglasess/sunglass.png"
glassPNG = cv2.imread(glassimagePath,-1)

# Resize the image to fit over the eye region
glassPNG = cv2.resize(glassPNG, None, fx=0.5, fy=0.5)
glassHeight, glassWidth, nChannels = glassPNG.shape
print("Sunglass Dimension ={}".format(glassPNG.shape))

# Separate the Color and alpha channels
glassBGR = glassPNG[:,:,0:3]
glassMask1 = glassPNG[:,:,3]

# Display the images for clarity
plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(glassBGR[:,:,::-1]);plt.title('Color channels');
plt.subplot(122);plt.imshow(glassMask1,cmap='gray');plt.title('Alpha channel');

# Top left corner of the glasses
topLeftRow = 130
topLeftCol = 130

bottomRightRow = topLeftRow + glassHeight
bottomRightCol = topLeftCol + glassWidth

# Get the eye region from the face image
eyeROI= faceWithGlassesBitwise[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]
# Make the dimensions of the mask same as the input image.
# Since Face Image is a 3-channel image, we create a 3 channel image for the mask
glassMask = cv2.merge((glassMask1,glassMask1,glassMask1))


# Use the mask to create the masked eye region
eye = cv2.bitwise_and(eyeROI,cv2.bitwise_not(glassMask))
# Use the mask to create the masked sunglass region
sunglass = cv2.bitwise_and(glassBGR,glassMask)

# Combine the Sunglass in the Eye Region to get the augmented image
eyeRoiFinal = cv2.bitwise_or(eye, sunglass)

# Replace the eye ROI with the output from the previous section
faceWithGlassesBitwise[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]=eyeRoiFinal

# Display the final result
plt.figure(figsize=[20,20]);
plt.subplot(121);plt.imshow(faceImage[:,:,::-1]); plt.title("Original Image");
plt.subplot(122);plt.imshow(faceWithGlassesBitwise[:,:,::-1]);plt.title("With Sunglasses");

plt.show()
