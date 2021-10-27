# Import libraries
import cv2
import numpy as np
#from dataPath import DATA_PATH
import matplotlib.pyplot as plt 	 	

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

image = cv2.imread("/home/paulstein/opencv/Example_course/PYHTON/SECTION 2/Boy_image_modify/boy.jpg")
plt.imshow(image[:,:,::-1])
imageCopy = image.copy()	

#Black pixels
emptyMatrix = np.zeros((100,200,3),dtype='uint8')
plt.imshow(emptyMatrix)


#White pixels
emptyMatrix = 255*np.ones((100,200,3),dtype='uint8')
plt.imshow(emptyMatrix)



#Empty pixels an size same as boy image
emptyOriginal = 100*np.ones_like(image)
plt.imshow(emptyOriginal)



plt.show()
