# Import cv2 module
import cv2

import matplotlib.pyplot as plt
import matplotlib
imageName = "/home/paulstein/opencv/Example_course/PYHTON/SECTION 4/boy.jpg"

# Load the image
image = cv2.imread(imageName, cv2.IMREAD_COLOR)


# Draw a line
imageLine = image.copy()


cv2.line(imageLine, (100, 80), (140, 80), (150, 150, 0), thickness=8, lineType=cv2.LINE_AA);
# Display the original image
plt.imshow(imageLine[:,:,::-1])
imageCircle = image.copy()
cv2.circle(imageCircle, (250, 100), 100, (180, 180, 0), thickness = 2, lineType=cv2.LINE_AA); #The "thickness number in negativo filles a circle"
plt.imshow(imageCircle[:,:,::-1])
#plt.show()

ellipsedImage = image.copy()
cv2.ellipse(ellipsedImage, (200, 100), (200, 100), 0 , 0 , 360, (0, 0, 255), thickness = 3, lineType = cv2.LINE_AA);#The "thickness number in negativo filles an ellipse"
plt.imshow(ellipsedImage[:,:,::-1])
cv2.ellipse(ellipsedImage, (200, 100), (200, 100), 90 , 0 , 360, (0, 255, 0), thickness = 3, lineType = cv2.LINE_AA);#The "thickness number in negativo filles an ellipse"
plt.imshow(ellipsedImage[:,:,::-1])
rectangleImage = image.copy()
cv2.rectangle(rectangleImage, (50, 80), (200, 300), (255,0,0), thickness = 3, lineType=cv2.LINE_AA);
plt.imshow(rectangleImage[:,:,:: -1])

#Obtain data to create a box to display a centered text
# Put text into image
imageText = image.copy()
text = "I am studying"
fontScale = 1.5
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontColor = (250, 10, 10)
fontThickness = 2

imageGetTextSize = image.copy()
imageHeight, imageWidth=imageGetTextSize.shape[:2]
# Get the text box height and width and also the baseLine
textSize, baseLine = cv2.getTextSize(text,fontFace,fontScale,fontThickness)
textWidth,textHeight = textSize
print("TextWidth = {}, TextHeight = {}, baseLine = {}".format(textWidth, textHeight, baseLine))

# Get the coordinates of text box bottom left corner
# The xccordinate will be such that the text is centered
xcoordinate = (imageWidth - textWidth)//2

# The y coordinate will be such that the entire box is just 10 pixels above the bottom of image
ycoordinate = (imageHeight - baseLine - 10)
print("TextBox Bottom Left = ({},{})".format(xcoordinate,ycoordinate))

# Draw the Canvas using a filled rectangle
canvasColor = (255, 255, 255)
canvasBottomLeft = (xcoordinate,ycoordinate+baseLine)
canvasTopRight = (xcoordinate+textWidth, ycoordinate-textHeight)
cv2.rectangle(imageGetTextSize, canvasBottomLeft, canvasTopRight, canvasColor, thickness=-1);
print("Canvas Bottom Left = {}, Top Right = {}".format(canvasBottomLeft,canvasTopRight))

# Now draw the baseline ( just for reference )
lineThickness = 2
lineLeft = (xcoordinate, ycoordinate)
lineRight = (xcoordinate+textWidth, ycoordinate)
lineColor = (0,255,0)
cv2.line(imageGetTextSize, lineLeft, lineRight, lineColor, thickness = lineThickness, lineType=cv2.LINE_AA);

# Finally Draw the text
cv2.putText(imageGetTextSize, text, (xcoordinate,ycoordinate), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA);

# Display the Output Image
plt.imshow(imageGetTextSize[...,::-1])
plt.show()
#plt.savefig("imageGetTextSize.png")

cv2.imwrite("imageGetTextSize.png",imageGetTextSize)

