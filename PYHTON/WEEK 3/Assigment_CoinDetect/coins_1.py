import cv2
import numpy as np
import cv2
import matplotlib.pyplot as plt 	 	

	
# Image path
imagePath = "/home/paulstein/opencv/Example_course/PYHTON/WEEK 3/Assigment_CoinDetect/coins_1.png"
# Read image
# Store it in the variable image
###
image = cv2.imread(imagePath)
cv2.imshow("Ecample", image)
cv2.waitKey(0)

###
dst = image.copy()
##Jupiter Notebook way of display 
##plt.imshow(image[:,:,::-1]);
##plt.title("Original Image")

#Terminal display image

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imageB, imageG, imageR = cv2.split(image)
	
cv2.imshow("Boy", image)
# Wait for user to press a key
cv2.waitKey(0)
# Destroy the window
#cv2.destroyAllWindows()
#cv2.imshow("Grayscale Image", imageB)
# Wait for user to press a key
#cv2.waitKey(0)
# Destroy the window
#cv2.destroyAllWindows()
cv2.imshow("Grayscale Image", imageG)
# Wait for user to press a key
cv2.waitKey(0)
# Destroy the window
#cv2.destroyAllWindows()
#cv2.imshow("Grayscale Image", imageR)
# Wait for user to press a key
#cv2.waitKey(0)
# Destroy the window
#cv2.destroyAllWindows()

###
#I have been trying the thresholding method with then different images, from the regular "image", "imageGray" and 
#the splited ones, getting the values in the next code that fits more the "Thresholded Image".

###
thresh = 25
maxValue = 247
dst = imageGray.copy()
th, dst = cv2.threshold(imageG, thresh, maxValue, cv2.THRESH_BINARY_INV)
# Display the thresholded image
###
plt.imshow(dst)
plt.title('my picture')
plt.show()
###
#In this first section we will perform dilation on the image
#First the assignation of the properties of the kernel element. 
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (11,11))
#Second we start performing dilation with the opencv function. We clean the image using a bigger kernel 
#instead of using iterations
dilatedImage = cv2.dilate(dst, element)
#In this second section we will perform Closing on the image previously dilated
#First we will especify the kernel size
kernelSize = 4

# Create Kernel
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*kernelSize+1, 2*kernelSize+1),
                                    (kernelSize, kernelSize))

# Perform Dilation
imDilated = cv2.dilate(dilatedImage, element)
# Perform Erosion
imClose = cv2.erode(imDilated, element)

# Display all the images obtained with our code
plt.figure(figsize=[30,100])
plt.subplot(131);plt.imshow(dilatedImage);plt.title("1. Dilated image");
plt.subplot(132);plt.imshow(imClose);plt.title("1. Closing image");
plt.show() 
# Get structuring element/kernel which will be used for dilation
### This second image is implemented with the iteratiosn of a smaller kernel than the previous one. 
# We iterate through the image three times
secondelement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
secondDilatedImage = cv2.dilate(dst, secondelement, iterations = 3)
###

#Then we proceed to clos the previous image dilated. COmpare with th other one we are includinf ITERATIONS and
#we are closing with CROOS instead of ELLIPSE and the Dilation it was performed with ELLIPSE instead of CROSS.

#First we will especify the kernel size
kernelSize = 3

# Create Kernel
secelement = cv2.getStructuringElement(cv2.MORPH_CROSS, (2*kernelSize+1, 2*kernelSize+1),
                                    (kernelSize, kernelSize))

# Perform Dilation
secimDilated = cv2.dilate(secondDilatedImage, element)
# Perform Erosion
secimClose = cv2.erode(secimDilated, element)

plt.figure(figsize=[30,100])
plt.subplot(131);plt.imshow(secondDilatedImage);plt.title("2. Dilated image");
plt.subplot(132);plt.imshow(secimClose);plt.title("2. Closing image");
plt.show() #The one displays the image
