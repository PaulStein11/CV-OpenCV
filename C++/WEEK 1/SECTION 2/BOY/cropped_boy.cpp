
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

using namespace std;
using namespace cv;

int main (){


Mat image = imread("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/boy.jpg",1);
Mat copiedImage = image.clone();
//PART1
// Crop out a rectangle
// x coordinates = 170 to 320
// y coordinates = 40 to 200
//Mat crop = image(Range(40,200),Range(170,320));
//imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/crop.png",crop);


//PART2
//copy the face to the left and to the right
//Mat copyRoi = image(Range(40,200),Range(180,320));
// Find height and width of the ROI
//int roiHeight = copyRoi.size().height;
//int roiWidth = copyRoi.size().width;
// Copy to left of Face
//copyRoi.copyTo(copiedImage(Range(40,40+roiHeight),Range(10,10+roiWidth)));
// Copy to right of Face
//copyRoi.copyTo(copiedImage(Range(40,40+roiHeight),Range(330,330+roiWidth)));
//imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/copiedRegions.png",copiedImage);


//PART3
//resize image
//int resizeDownWidth = 300;
//int resizeDownHeight = 200;
//Mat resizedDown;
//resize(image, resizedDown, Size(resizeDownWidth, resizeDownHeight), INTER_LINEAR);
// Mess up with the aspect ratio
//int resizeUpWidth = 600;
//int resizeUpHeight = 900;
//Mat resizedUp;
//resize(image, resizedUp, Size(resizeUpWidth, resizeUpHeight), INTER_LINEAR);
//imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/resizedUp.png",resizedUp);
//imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/resizedDown.png",resizedDown);


//PART4
// Create an empty image of same size as the original
//Mat mask1 = Mat::zeros(image.size(), image.type());
//imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/mask1.png",mask1);

//mask1(Range(50,200),Range(170,320)).setTo(255);
//imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/mask1Revised.png",mask1);

//PART5
//Create a mask based on the colors in the image
Mat mask2;
inRange(image, Scalar(0,0,150), Scalar(100,100,255), mask2);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/mask2.png",mask2);
}


