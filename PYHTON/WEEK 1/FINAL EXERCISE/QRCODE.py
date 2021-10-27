#CROPPING AND PASTING QR CODE
# Import cv2 module
import cv2
import matplotlib.pyplot as plt
import matplotlib
imageName = "/home/paulstein/opencv/Example_course/PYHTON/FINAL EXERCISE/QRCODE.png"
#imageID = "/home/paulstein/opencv/Example_course/PYHTON/FINAL EXERCISE/IDCard-Template.png"
# Load the image
image = cv2.imread(imageName, -1)
#imageID = cv2.imread(imageID, cv2.IMREAD_COLOR)
plt.imshow(image[:,:,::-1])
#plt.imshow(imageID[:,:,::-1])
#crop = image[170:170,1450:170]
#plt.imshow(crop[:,:,::-1])


#copiedImage = imageID.copy()

copiedImage[int(12, 72), int(135,198)] = imageName
plt.imshow(copiedImage[:,:,::-1])
plt.show()
