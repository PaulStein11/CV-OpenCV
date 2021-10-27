#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;



int main() {

// Load the Face Image
string imagepath = ("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/musk.jpg");
Mat faceImage = imread(imagepath);


//Make a copy

Mat faceWithGlassesBitwise = faceImage.clone();

//Read sunglasses image in Alpha Channel
string glassespath = ("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/sunglass.png");
Mat glassPNG = imread(glassespath, -1);

// Resize the image to fit over the eye region

resize(glassPNG,glassPNG, Size(300,100));
cout << "image Dimension = " << glassPNG.size() << endl;

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
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/sunglassRGB.png",glassBGR);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/sunglassAlpha.png",glassMask1);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Get the eye region from the face image
Mat eyeROI = faceWithGlassesBitwise(Range(150,250),Range(140,440));

// Make the dimensions of the mask same as the input image.
// Since Face Image is a 3-channel image, we create a 3 channel image for the mask
Mat glassMask;
Mat glassMaskChannels[] = {glassMask1,glassMask1,glassMask1};
merge(glassMaskChannels,3,glassMask);

// Use the mask to create the masked eye region
Mat eye;
Mat glassMaskNOT;
bitwise_not(glassMask1, glassMaskNOT);

Mat eyeChannels[3];
Mat eyeROIChannels[3];
Mat maskedGlass;
Mat eyeRoiFinal;

split(eyeROI,eyeROIChannels);

for (int i = 0; i < 3; i++)
{
    bitwise_and(eyeROIChannels[i], glassMaskNOT, eyeChannels[i]);
}

merge(eyeChannels,3,eye);

imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/glassMaskNOT.png",glassMaskNOT);

Mat glassMaskNOTChannels[] = {glassMaskNOT,glassMaskNOT,glassMaskNOT};
Mat glassMaskNOTMerged;
merge(glassMaskNOTChannels,3,glassMaskNOTMerged);

bitwise_and(eyeROI, glassMaskNOTMerged, eye);
// Use the mask to create the masked sunglass region
Mat sunglass;
Mat sunglassChannels[3];
Mat glassBGRChannels[3];

split(glassBGR,glassBGRChannels);

for (int i=0; i < 3; i++)
    bitwise_and(glassBGRChannels[i], glassMask1, sunglassChannels[i]);

merge(sunglassChannels,3,sunglass);
multiply(glassBGR, glassMask, maskedGlass);

// Combine the Sunglass in the Eye Region to get the augmented image
bitwise_or(eye, sunglass, eyeRoiFinal);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/maskedEyeRegionBitwise.png",eye);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/maskedSunglassRegionBitwise.png",sunglass);
imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/augmentedEyeAndSunglassBitwise.png",eyeRoiFinal);


// Replace the eye ROI with the output from the previous section
eyeRoiFinal.copyTo(eyeROI);

imwrite("/home/paulstein/opencv/Example_course/C++/WEEK 1/SECTION 5/Bitwise example_ MUSKGlass/withSunglassesBitwise.png",faceWithGlassesBitwise);

}
