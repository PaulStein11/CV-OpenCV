# Import module
import cv2
import matplotlib.pyplot as plt
import matplotlib

cap = cv2.VideoCapture("/home/paulstein/opencv/Example_course/PYHTON/WEEK 2/SECTION 1/week2-python/chaplin.mp4")

if(cap.isOpened() == False):
   print("Error while opening video stream or file")


# Default resolutions of the frame are obtained.
# Convert the resolutions from float to integer.
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object.
# The output is stored in 'outputChaplin.avi' file.
out = cv2.VideoWriter('outputChaplin.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 25, (frame_width,frame_height))

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
    
  if ret == True:
    
    # Write the frame into the file 'outputChaplin.avi'
    out.write(frame)
    
    # Wait for 25 ms before moving on to the next frame
    cv2.imshow("Frame",frame)
    cv2.waitKey(10)
    
  # Break the loop
  else: 
    break

# When everything done, release the VideoCapture and VideoWriter objects
cap.release()
out.release()


