#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {

  // Load the Face Image
string faceImagePath =("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/musk.jpg");
//Read the image
Mat faceImage = imread(faceImagePath);
string glassimagePath = ("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/sunglass.png");

// Read the image
Mat glassPNG = imread(glassimagePath,-1);
// Resize the image to fit over the eye region
resize(glassPNG,glassPNG, Size(300,100));
cout << "Image Dimension = " << glassPNG.size() << endl;
cout << "Number of channels = " << glassPNG.channels();


// Separate the Color and alpha channels
Mat glassRGBAChannels[4];
Mat glassRGBChannels[3];
split(glassPNG, glassRGBAChannels);
for (int i = 0; i < 3; i++){
    // Copy R,G,B channel from RGBA to RGB
    glassRGBChannels[i] = glassRGBAChannels[i];
}
Mat glassBGR, glassMask1;
// Prepare BGR Image
merge(glassRGBChannels,3,glassBGR);
// Alpha channel is the 4th channel in RGBA Image
glassMask1 = glassRGBAChannels[3];
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/sunglassRGB.png",glassBGR);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/sunglassAlpha.png",glassMask1);


// Make a copy
Mat faceWithGlassesNaive = faceImage.clone();
Mat roiFace =  faceWithGlassesNaive(Range(150,250),Range(140,440));
// Replace the eye region with the sunglass image
glassBGR.copyTo(roiFace);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/faceWithGlassesNaive.png",faceWithGlassesNaive);

// Make the dimensions of the mask same as the input image.
// Since Face Image is a 3-channel image, we create a 3 channel image for the mask
Mat glassMask;
Mat glassMaskChannels[] = {glassMask1,glassMask1,glassMask1};
merge(glassMaskChannels,3,glassMask);
// Make the values [0,1] since we are using arithmetic operations
glassMask = glassMask/255;
// Make a copy
Mat faceWithGlassesArithmetic = faceImage.clone();
// Get the eye region from the face image
Mat eyeROI = faceWithGlassesArithmetic(Range(150,250),Range(140,440));

Mat eyeROIChannels[3];
split(eyeROI,eyeROIChannels);
Mat maskedEyeChannels[3];
Mat maskedEye;

for (int i = 0; i < 3; i++)
{
    // Use the mask to create the masked eye region
    multiply(eyeROIChannels[i], (1-glassMaskChannels[i]), maskedEyeChannels[i]);
}

merge(maskedEyeChannels,3,maskedEye);

Mat maskedGlass;
// Use the mask to create the masked sunglass region
multiply(glassBGR, glassMask, maskedGlass);

Mat eyeRoiFinal;
// Combine the Sunglass in the Eye Region to get the augmented image
add(maskedEye, maskedGlass, eyeRoiFinal);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/maskedEyeRegion.png",maskedEye);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/maskedSunglassRegion.png",maskedGlass);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/augmentedEyeAndSunglass.png",eyeRoiFinal);

// Replace the eye ROI with the output from the previous section
eyeRoiFinal.copyTo(eyeROI);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 4/withSunglasses.png",faceWithGlassesArithmetic);

}
