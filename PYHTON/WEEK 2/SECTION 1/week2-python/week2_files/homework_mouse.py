import cv2
import math

refPt = []
cropping = []

def click_and_crop(action, x, y, flags, userdata):
	# grab references to the global variables
	global refPt, cropping
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if action == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		#cropping = True

	# check to see if the left mouse button was released
	elif action == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		#cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (255, 0, 0), 1)
		cv2.imshow("image", image)
image = cv2.imread("sample.jpg",1)
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
k = 0
# keep looping until the 'ESC' key is pressed
while k!= 27:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	cv2.putText(image,"Choose top lef corner, and drag,?", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255), 2 );
	k = cv2.waitKey(20) & 0xFF
if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()
