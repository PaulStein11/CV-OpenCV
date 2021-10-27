
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>


using namespace cv;
using namespace std;



string imagePath = DATA_PATH + "/home/paulstein/opencv/Example_course/C++/ZERO IMAGE/number_zero.jpg";

// Read image in Grayscale format
Mat testImage = imread(imagePath,0);

cout << testImage;

