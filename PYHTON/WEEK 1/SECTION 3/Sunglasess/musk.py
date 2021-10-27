import cv2
import numpy as np
import matplotlib.pyplot as plt 	 	
import matplotlib


# Read image
faceImagePath ="/home/paulstein/opencv/Example_course/PYHTON/SECTION 3/Sunglasess/musk.jpg"
faceImage = cv2.imread(faceImagePath)
faceImage = np.float32(faceImage)/255  #Conver to float32 from uint8

plt.imshow(faceImage[:,:,::-1]);plt.title("Face")
#plt.show()

# Load the Sunglass image with Alpha channel
# (http://pluspng.com/sunglass-png-1104.html)
glassimagePath = "/home/paulstein/opencv/Example_course/PYHTON/SECTION 3/Sunglasess/sunglass.png"
glassPNG = cv2.imread(glassimagePath,-1)
glassPNG = np.float32(glassPNG)/255

# Resize the image to fit over the eye region
glassPNG = cv2.resize(glassPNG, None, fx=0.5, fy=0.5)
glassHeight, glassWidth, nChannels = glassPNG.shape
print("Sunglass dimension ={}".format(glassPNG.shape))

# Separate the Color and alpha channels
glassBGR = glassPNG[:,:,0:3]
glassMask1 = glassPNG[:,:,3]

# Display the images for clarity
plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(glassBGR[:,:,::-1]);plt.title('Sunglass Color channels');
plt.subplot(122);plt.imshow(glassMask1,cmap='gray');plt.title('Sunglass Alpha channel');

## --- REPLACE THE SELECTED REGION OF THE EYES TO THE PNG GLASSES
# Top left corner of the glasses
topLeftRow = 130
topLeftCol = 130

bottomRightRow = topLeftRow + glassHeight
bottomRightCol = topLeftCol + glassWidth

# Make a copy
faceWithGlassesNaive = faceImage.copy()

# Replace the eye region with the sunglass image
faceWithGlassesNaive[topLeftRow:bottomRightRow,topLeftCol:bottomRightCol]=glassBGR

plt.imshow(faceWithGlassesNaive[...,::-1])
plt.show()

# ---------------------------FIXING THIS PROBLEM

    #1.Create an alpha mask with 3-channels using the single channel mask.
    #2.Extract the eye region from the face image
    #3.Multiply the Mask with the sunglass to get the masked sunglass
    #4.Multiply the negative of Mask with the eye region to create a hole in the eye region for the sunglass to be placed.
    #5.Add the masked sunglass and eye regions to get the combined eye region with the sunglass.
    #6.Replace the eye region in the original image with that of the output we got in the previous step. This is the final output

# Make the dimensions of the mask same as the input image.
# Since Face Image is a 3-channel image, we create a 3 channel image for the mask
glassMask = cv2.merge((glassMask1,glassMask1,glassMask1))

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








