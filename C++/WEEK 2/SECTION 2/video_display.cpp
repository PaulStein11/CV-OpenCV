#include <opencv2/videoio.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <string> 
#include <iostream>

using namespace std;
using namespace cv;

int main(void)
{
  // Open webcam
  VideoCapture cap(0);
  Mat frame;
  int k=0;
  // Detect if webcam is working properly
  if(!cap.isOpened())
  {
    cout<<"Unable to detect webcam "<<"\n";
    return 0;
  }
  else
  {
     while(1)
     {
        // Capture frame
        cap>>frame;
          if(k==27)
            break;
        // The following if-else block is used to check which key is pressed.
        // We use the waitKey() function to detect the input and 
        // respond only if either ‘e’ or ‘z’ is pressed. 
        // ‘ESC’(ASCII code = 27) is used to exit the program.
         
        // Identify if 'e' or 'E' is pressed
        if(k==101 || k==69)
            putText(frame, "E is pressed, press Z or ESC", Point(100,180), FONT_HERSHEY_SIMPLEX, 1, Scalar(0,255,0), 3);
        // Identify if 'z' or 'Z' is pressed or not
        if(k==90 || k==122)
            putText(frame, "Z is pressed", Point(100,180), FONT_HERSHEY_SIMPLEX, 1, Scalar(0,255,0), 3);
        imshow("Image",frame);
        // Waitkey is increased so that the display is shown
        k= waitKey(10000) & 0xFF;
     }
  }
  cap.release();
  destroyAllWindows();

}

