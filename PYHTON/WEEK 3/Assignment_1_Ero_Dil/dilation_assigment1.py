import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

im = np.zeros((10,10),dtype='uint8')
im[0,1] = 1
im[-1,0]= 1
im[-2,-1]=1
im[2,2] = 1
im[5:8,5:8] = 1

print(im)
plt.imshow(im)
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
ksize = element.shape[0]
height,width = im.shape[:2]
print(element)

dilatedEllipseKernel = cv2.dilate(im, element)

border = ksize//2
paddedIm = np.zeros((height + border*2, width + border*2))
paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
paddedDilatedIm = paddedIm.copy()

# Create a VideoWriter object
###
out_dilated = cv2.VideoWriter("dilationScratch.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 10, (320,240))
###

for h_i in range(border, height+border):
    for w_i in range(border,width+border):
        ###
        if im[h_i-border,w_i-border]:
            print("White Pixel Found @ {},{}".format(h_i,w_i))

            paddedIm[ h_i - border : (h_i + border)+1, w_i - border : (w_i + border)+1] = \
                cv2.bitwise_or(paddedIm[ h_i - border : (h_i + border)+1, w_i - border : (w_i + border)+1],element)
            # Print the intermediate result
            print(paddedIm)

        resized_image = cv2.resize(paddedIm, (50, 50), interpolation= cv2.INTER_LINEAR)
        ###
        # Convert resizedFrame to BGR before writing
        ###
        resized_image[:,0] = np.ones([1,1])/255.0
        resized_image[:,1] = np.ones([1,1])/255.0
# Release the VideoWriter object
###
out_dilated.release()
###
print(resized_image)
