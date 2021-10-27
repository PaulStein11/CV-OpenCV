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
matplotlib.rcParams['image.cmap'] = 'gray' #////////MAKES IMAGES GRAYSCALE INSTEAD OF GRB Binary OUTPUT
#create a black same sieze image
mask1 = np.zeros_like(image)
#plt.imshow(mask1)

mask1[50:200,170:320] = 255
plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image")
plt.subplot(122);plt.imshow(mask1[:,:,::-1]);plt.title("Mask")
print(mask1.dtype)

#-----------------------------------------------

mask2 = cv2.inRange(image, (0,0,150), (100,100,255))
plt.figure(figsize=[15,15])
plt.subplot(121);plt.imshow(image[...,::-1]);plt.title("Original Image")
plt.subplot(122);plt.imshow(mask2);plt.title("Masked Image")





plt.show()
