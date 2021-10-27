#include <opencv2/opencv.hpp>
#include <opencv2/objdetect.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <string>


using namespace std;
using namespace cv;

int main(int argc, char* argv[]){

// Image Path
string imgPath =("/home/paulstein/opencv/Example_course/C++/WEEK 1/FINAL EXERCISE/IDCard-Satya.png");
// Read image and store it in variable img
Mat img = imread(imgPath);
//Detect QRcode
Mat bbox, rectifiedImage;

// Create a QRCodeDetector Object
// Variable name should be qrDecoder

QRCodeDetector qrDecoder = QRCodeDetector();
 
string opencvData = qrDecoder.detectAndDecode(img, bbox, rectifiedImage);


// Check if a QR Code has been detected
if(opencvData.length()>0)
    cout << "QR Code Detected" << endl;
else
    cout << "QR Code NOT Detected" << endl;


int n = bbox.rows;

// Draw the bounding box
for(int i = 0 ; i < n ; i++)
  {
    line(img, Point2i(bbox.at<float>(i,0),bbox.at<float>(i,1)), Point2i(bbox.at<float>((i+1) % n,0), bbox.at<float>((i+1) % n,1)), Scalar(255,0,0), 3);
  }


 putText(img, string (opencvData), Point(10,100), FONT_HERSHEY_COMPLEX_SMALL, 1, Scalar(0,143,143), 2);

  //namedWindow("Result",CV_WINDOW_AUTOSIZE);
  imshow("Result", img);
  imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/FINAL EXERCISE/QRCode-Output.png",img)

waitKey(0);   

/// YOUR CODE HERE
///

}
