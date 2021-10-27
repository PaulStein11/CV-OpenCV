# Import module
import cv2
import matplotlib.pyplot as plt
import matplotlib

cap = cv2.VideoCapture("/home/paulstein/opencv/Example_course/PYHTON/WEEK 2/SECTION 1/week2-python/chaplin.mp4")

if(cap.isOpened() == False):
   print("Error while opening video stream or file")


# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  if ret == True:
    cv2.imshow("Video Output", frame)    
    # Wait for 25 ms before moving on to the next frame
    # This will slow down the video
    cv2.waitKey(25)

  # Break the loop
  else: 
    break

plt.imshow(frame[...,::-1])

plt.show()

