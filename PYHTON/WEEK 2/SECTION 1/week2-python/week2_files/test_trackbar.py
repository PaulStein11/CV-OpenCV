import cv2

maxScaleUp = 100
scaleFactor = 1
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

# load an image
im = cv2.imread("truth.png")

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

def scaleImage(*args):
    global scaleFactor
    global scaleType
    scaleFactor = 1+ args[0]/100.0
    if scaleFactor == 0:
        scaleFactor = 1
    scaledImage = cv2.resize(im, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_AREA)
    cv2.imshow(windowName, scaledImage)
cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleImage)

def downscaleImage(*args):
    global scaleFactor
    global scaleType
    scaleFactor = 1 - args[0]/100.0
    if scaleFactor == 0:
        scaleFactor = 1
    downscaledImage = cv2.resize(im, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_AREA)
    cv2.imshow(windowName, downscaledImage)

cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, downscaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, downscaleImage)

while True:
    c = cv2.waitKey(20)
    if c==27:
        break

    s = cv2.getTrackbarPos(trackbarType, windowName)

    if s == 0:
        scaleImage()
    elif s == 1:
        downscaleImage()

cv2.destroyAllWindows()
