import numpy as np
import cv2
from matplotlib import pyplot as plt



img = cv2.imread('/home/paulstein/opencv/Example_course/PYHTON/WEEK 1/SECTION 1/MUSK/musk.jpg')

#imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  //Converts BGR 2 RGB
#plt.imshow(imgRGB)
#plt.imshow(img[:,:,::-1])  #It will reverse the order of the 3rd dimension i.e. channels
#plt.imshow(img)

#plt.figure(figsize=[20,5])

#plt.subplot(131);plt.imshow(img[:,:,0]);plt.title("Blue Channel");
#plt.subplot(132);plt.imshow(img[:,:,1]);plt.title("Green Channel");
#plt.subplot(133);plt.imshow(img[:,:,2]);plt.title("Red Channel");
#plt.show() #The one displays the image

##        -------------------------------------------------------------------------------------


# Split the image into the B,G,R components
b,g,r = cv2.split(img)

# Show the channels
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(b);plt.title("Blue Channel");
plt.subplot(142);plt.imshow(g);plt.title("Green Channel");
plt.subplot(143);plt.imshow(r);plt.title("Red Channel");

# Merge the individual channels into a BGR image
imgMerged = cv2.merge((b,g,r))
# Show the merged output
plt.subplot(144);plt.imshow(imgMerged[:,:,::-1]);plt.title("Merged Output");

plt.show() #The one displays the image

