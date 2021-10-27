# Import module
import cv2
import matplotlib.pyplot as plt
import matplotlib

cap = cv2.VideoCapture("/home/paulstein/opencv/Example_course/PYHTON/WEEK 2/SECTION 1/week2-python/chaplin.mp4")

if(cap.isOpened() == False):
   print("Error while opening video stream or file")

#Get properties from a video

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(width,height)

# Set position of video to 2.5 seconds
ret = cap.set(cv2.CAP_PROP_POS_MSEC, 2500)
print(ret)
# Width set differently
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
print(ret)
# Height set differently
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
print(ret)
#Display the videoFrame
ret, frame = cap.read()
plt.imshow(frame[...,::-1])
cap.release()
plt.show()


