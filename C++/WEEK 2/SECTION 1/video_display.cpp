#include "opencv2/opencv.hpp"
#include <iostream>
//#include "displayImages.h"
//#include "matplotlibcpp.h"

using namespace std;
using namespace cv;
//using namespace matplotlibcpp;

int main(){


VideoCapture cap("/home/paulstein/opencv/Example_course/C++/WEEK 2/SECTION 1/chaplin.mp4");
int frame_width = cap.get(CAP_PROP_FRAME_WIDTH);
int frame_height = cap.get(CAP_PROP_FRAME_HEIGHT);

// Define the codec and create VideoWriter object.
// The output is stored in 'outputChaplin.mp4' file.

VideoWriter out("/home/paulstein/opencv/Example_course/C++/WEEK 2/SECTION 1/outputChaplin.mp4",VideoWriter::fourcc('M','J','P','G'),10, Size(frame_width,frame_height));

// Read until video is completed
while(cap.isOpened()){

    Mat frame;

    // Capture frame-by-frame
    cap >> frame;

    // If the frame is empty, break immediately
    if (frame.empty())
      break;

    // Write the frame into the file 'outputChaplin.mp4'
    out.write(frame);
    imshow("Frame",frame);
    // Wait for 25 ms before moving on to the next frame
    // This will slow down the video 
    waitKey(25);
}

// When everything done, release the VideoCapture and VideoWriter objects
cap.release();
out.release();


}
