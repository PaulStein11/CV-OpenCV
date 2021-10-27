# Import cv2 module
import cv2
import matplotlib.pyplot as plt
#import numpy as np
import matplotlib

imgPath ="/home/paulstein/opencv/Example_course/PYHTON/WEEK 1/FINAL EXERCISE/IDCard-Monica.png"
img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

plt.imshow(img[:,:,:: -1])
#plt.show()

qrDecode = cv2.QRCodeDetector()
opencvData, bbox, rectifiedImage = qrDecode.detectAndDecode(img)
if len(opencvData) >0:
    print("QR Code Detected")
    print("Decoded Data : {}".format(opencvData))
    #display(image, bbox)
    #rectifiedImage = np.uint8(rectifiedImage);
else:
    print("QR Code NOT Detected")
    cv2.imshow("Results", img)

#def display(image, bbox):
n = len(bbox)
for j in range(n):
    cv2.line(img, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3);
 
# Display results
resultImagePath = "QRCode-Output.png"
cv2.imwrite(resultImagePath, img)
plt.imshow(img[:,:,:: -1])
plt.show()



