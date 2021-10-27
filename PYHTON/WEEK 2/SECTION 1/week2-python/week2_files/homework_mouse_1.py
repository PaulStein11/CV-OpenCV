import cv2
import math

#Creating variables for the rectangle cropping action
cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0

image = cv2.imread("sample.jpg",1)
oriImage = image.copy()

def mouse_crop(action, x, y, flags, userdata):
    # Referencing global variables
    global x_start, y_start, x_end, y_end, cropping
    # Action to be taken when left mouse button is pressed
    # if the left mouse button was DOWN, start RECORDING
    if action == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif action == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif action == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.waitKey(20) & 0xFF
            cv2.imwrite("Cropped.png", roi)

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)
k = 0
while k!=27:

    i = image.copy()

    if not cropping:
        cv2.imshow("image", image)
        cv2.putText(image,"Choose top lef corner, and drag,?", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255), 2 );	    k = cv2.waitKey(20) & 0xFF

    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow("image", i)
        cv2.waitKey(1)

# close all open windows
cv2.destroyAllWindows()
