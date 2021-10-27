
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

using namespace std;
using namespace cv;

int main (){


//Mat image = imread("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/boy.jpg");


// Create a new image by copying the already present image using the clone operation
//Mat imageCopy = image.clone();


Mat emptyMatrix = Mat(100,200,CV_8UC3, Scalar(0,0,0));
//imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/emptyMatrix.png",emptyMatrix);
emptyMatrix.setTo(Scalar(255,255,255));
//imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/emptyMatrixWhite.png",emptyMatrix);


Mat emptyOriginal = Mat(emptyMatrix.size(), emptyMatrix.type(), Scalar(100,100,100));
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 2/BOY/emptyMatrix100.png",emptyOriginal);






}


