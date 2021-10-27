#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <vector>
#include <iostream>
#include <math.h>

using namespace cv;
using namespace std;

// Points to store the top left and a point on the bottom right
Point top_left, bottom_right;
// Source image
Mat source;

// function which will be called on mouse input
void drawRectangle(int action, int x, int y, int flags, void *userdata)
{

// Action to be taken when left mouse button is pressed
  if( action == EVENT_LBUTTONDOWN )
  {
    rec = Point(x , y);
//Mark left top corner
    rectangle(source, rec, Scalar(255, 0, 255), 3, LINE_8);
}
// Action to be taken when left mouse button is released
  else if ( action == EVENT_LBUTTONUP)
  {
    bottom_right = Point(x, y);
//Mark bottom right corner
    rectangle(source, bottom_right, Scalar(255, 0, 255), 3, LINE_8);
}

}

int main(void)
{

   source = imread("/home/paulstein/opencv/Example_course/C++/WEEK 2/SECTION 3/build/sample.jpg",1);
  // Make a dummy image, will be useful to clear the drawing
   Mat dummy = source.clone();
   namedWindow("Window");
  // highgui function called when mouse events occur
  setMouseCallback("Window", drawRectangle);

  int k=0;

  // loop until escape character is pressed
  while(k!=27)
  {
    imshow("Window", source );
    putText(source,"Choose , and drag, ?" ,Point(10,30), FONT_HERSHEY_SIMPLEX, 0.7,Scalar(255,255,255), 2 );
    k= waitKey(20) & 0xFF;
    if(k== 99)
            // Another way of cloning
            dummy.copyTo(source);
  }
  return 0;
}


}
