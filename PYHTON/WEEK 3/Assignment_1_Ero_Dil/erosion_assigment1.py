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

erodedEllipseKernel = cv2.erode(im, element)

border = ksize//2
paddedIm = np.zeros((height + border*2, width + border*2))
paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
paddedErodedIm = paddedIm.copy()

# Create a VideoWriter object
###
outAvi = cv2.VideoWriter("erotionScratch.avi",cv2.VideoWriter_fourcc(*'MP4V'), 10,(50,50))
###

for h_i in range(border, height+border):
    for w_i in range(border,width+border):
        ###
        if im[h_i-border,w_i-border]:
            print("White Pixel Found @ {},{}".format(h_i,w_i))

            paddedIm[ h_i - border : (h_i + border)+1, w_i - border : (w_i + border)+1] = \
                cv2.bitwise_or(paddedIm[ h_i - border : (h_i + border)+1, w_i - border : (w_i + border)+1],element)

        # Resize output to 50x50 before writing it to the video
        ###
        frame_width = 50
        frame_height = 50
        resizedFrame = cv2.resize(im,(50,50),interpolation = cv2.INTER_LINEAR)
        ###
        # Convert resizedFrame to BGR before writing
        ###
        convert_to_BGR = cv2.cvtColor(resizedFrame, cv2.COLOR_GRAY2BGR)
        ###

# Release the VideoWriter object
###
plt.imshow(paddedIm);plt.show()
outAvi.release()
###
erosedImage = paddedIm[border:border+height,border:border+width]
plt.imshow(erosedImage)
print(erosedImage)
