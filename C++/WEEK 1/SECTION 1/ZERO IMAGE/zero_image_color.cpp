
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>


using namespace cv;
using namespace std;



int main() {

string imagePath = "/home/paulstein/opencv/Example_course/C++/ZERO IMAGE/number_zero.jpg";
Mat testImage = imread(imagePath,1);

testImage(Range(0,3),Range(0,3)).setTo(Scalar(255,0,0));
testImage(Range(3,6),Range(0,3)).setTo(Scalar(0,255,0));
testImage(Range(6,9),Range(0,3)).setTo(Scalar(0,0,255));



imwrite("zeroModified.png",testImage);

return 0;
}
