#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>

using namespace std;
using namespace cv;

int main(){

//Open and read image

string imagePath = ("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/Exercise/musk.jpg");
Mat image_musk = imread(imagePath);

string imagePathmoustache = ("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/Exercise/Moustache.png");
Mat image_moustache = imread(imagePathmoustache, -1);

// Resize the image to fit over the eye region
resize(image_moustache, image_moustache, Size (100, 50));
cout << "The size of the mustache is: " << image_moustache.size() << endl;
cout << "The number of channels are: " << image_moustache.channels() << endl;


// Separate the Color and alpha channels
Mat moustacheRGBA_channel [4];
Mat moustacheRGB_channel [3];

split(image_moustache, moustacheRGBA_channel);

for(int i = 0; i < 3; i++){

 //Copy R, G, B channel from RGBA to RGB
   moustacheRGB_channel[i] = moustacheRGBA_channel[i];
} 

Mat moustacheBGR, moustacheMask1;
// Prepare BGR Image
merge(moustacheRGB_channel, 3, moustacheBGR);

// Alpha channel is the 4th channel in RGBA Image
moustacheMask1 = moustacheRGBA_channel[3];

imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/Exercise/moustacheRGB.png", moustacheBGR);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/Exercise/moustacheAlpha.png", moustacheMask1);

//Make a copy
Mat facemoustacheNaivee = image_musk.clone();
Mat roiFace = facemoustacheNaivee(Range(150, 250), Range(140, 440));

moustacheBGR.copyTo(roiFace);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/Exercise/facemoustache.png", facemoustacheNaivee);






}

/*

// Make a copy
Mat faceWithGlassesNaive = faceImage.clone();
Mat roiFace =  faceWithGlassesNaive(Range(150,250),Range(140,440));
// Replace the eye region with the sunglass image
glassBGR.copyTo(roiFace);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/faceWithGlassesNaive.png",faceWithGlassesNaive);
*/
