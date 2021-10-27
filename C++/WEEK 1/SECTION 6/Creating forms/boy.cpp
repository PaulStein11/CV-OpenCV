#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

using namespace std;

using namespace cv;


int main(){

// Path to the image we are going to read
// This can be an absolute or relative path
// Here we are using a relative path
string imageName = ("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 6/Creating forms/boy.jpg");

// Load the image
Mat image;
image = imread(imageName, IMREAD_COLOR);

//To display the image function

// Draw a line
Mat imageLine = image.clone();

// The line starts from (322,179) and ends at (400,183)
// The color of the line is RED (Recall that OpenCV uses BGR format)
// Thickness of line is 5px
// Linetype is LINE_AA

line(imageLine, Point(200, 80), Point(280, 80), Scalar(255, 0, 0), 3, LINE_AA);

imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 6/Creating forms/line.jpg",imageLine);

//Circle
Mat imageCircle = image.clone();

circle(imageCircle, Point(250, 125), 100, Scalar(100, 255, 0), -2, LINE_AA); // The thickness of the circle, in this case 2 as positive, fill create an empty circle. negative it will create a filled one
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 6/Creating forms/circle.jpg",imageCircle);


//Ellipse
// Note: Ellipse Centers and Axis lengths must be integers
Mat imageEllipse = image.clone();

ellipse(imageEllipse, Point(250, 125), Point(100, 50), 0, 0, 360, 
        Scalar(255, 0, 0), 2, LINE_AA);

ellipse(imageEllipse, Point(250, 125), Point(100, 50), 90, 0, 360,
        Scalar(0, 255, 10), 2, LINE_AA);

imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 6/Creating forms/ellipse.jpg",imageEllipse);




// Draw an ellipse
// Note: Ellipse Centers and Axis lengths must be integers
imageEllipse = image.clone();

// Incomplete/Open ellipse
ellipse(imageEllipse, Point(250, 125), Point(100, 50), 0, 180, 360, 
        Scalar(255, 0, 0), 3, LINE_AA);

// Filled ellipse
ellipse(imageEllipse, Point(250, 125), Point(100, 50), 0, 0, 180, 
        Scalar(0, 0, 255), -2, LINE_AA); // Negative number always refer to a filled figure

imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 6/Creating forms/ellipseFilled.jpg",imageEllipse);

// Draw a rectangle (thickness is a positive integer)
Mat imageRectangle = image.clone();
rectangle(imageRectangle, Point(170, 50), Point(300, 200), 
          Scalar(255, 0, 255), 5, LINE_8);

imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 6/Creating forms/rectangle.jpg",imageRectangle);

// Create a window for display.
 namedWindow( "Display window", WINDOW_AUTOSIZE ); 
 imshow( "Display window", imageRectangle );                // Show our image inside it.
 waitKey(0); 
}


