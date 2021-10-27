
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>


using namespace cv;
using namespace std;

int main(void){
string imagePath =  ("/home/paulstein/opencv/Example_course/C++/MUSK IMAGE/musk.jpg");

//DISPLAYS THE SIZE OF THE IMAGE
Mat img = imread(imagePath);
//cout << "image size = " << img.size();



// Show the channels
Mat imgChannels[3];
split(img, imgChannels);

// Write the channels and creates more images. Creates them ib the place where is executed but before the ex: "imgBlue.png" you can add any kind of path
imwrite("imgBlue.png",imgChannels[0]);
imwrite("imgGreen.png",imgChannels[1]);
imwrite("imgRed.png",imgChannels[2]);


return 0;

}
