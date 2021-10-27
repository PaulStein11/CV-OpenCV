
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>


using namespace cv;
using namespace std;



int main() {
string imagePath = "/home/paulstein/opencv/Example_course/C++/ZERO IMAGE/number_zero.jpg";

// Read image in Grayscale format
Mat testImage = imread(imagePath,0);

//Changes the MATRIZ image to a 200 in the row/column 0, 0
//testImage.at<uchar>(1,2)=200; 

//Select region in MAT
//Mat test_roi = testImage(Range(0,2),Range(0,4));
//cout << "Original Matrix\n" << testImage << endl << endl;

//cout << "Selected Region\n" << test_roi;

//SELECT REGION IN MAT AND CHANGES
//testImage(Range(0,2),Range(0,4)).setTo(111);

//cout << "Modified Matrix\n" << testImage;

return 0;
}
