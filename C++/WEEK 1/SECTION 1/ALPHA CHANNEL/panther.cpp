

#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>


using namespace cv;
using namespace std;

int main(){
// Path of the PNG image to be loaded
string imagePath = "/home/paulstein/opencv/Example_course/C++/ALPHA CHANNEL/panther.png";

// Read the image
// Note that we are passing flag = -1 while reading the image ( it will read the image as is)
Mat imgPNG = imread(imagePath,-1);
cout << "image size = " << imgPNG.size() << endl;
cout << "number of channels = " << imgPNG.channels() << endl;

Mat imgBGR;
Mat imgPNGChannels[4];
split(imgPNG,imgPNGChannels);

merge(imgPNGChannels,3,imgBGR);

Mat imgMask = imgPNGChannels[3];

imwrite("colorChannels.png",imgBGR);
imwrite("alphaChannel.png",imgMask);

}
