# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/build"

# Include any dependencies generated for this target.
include CMakeFiles/using_the_mouse_for_annotation.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/using_the_mouse_for_annotation.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/using_the_mouse_for_annotation.dir/flags.make

CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o: CMakeFiles/using_the_mouse_for_annotation.dir/flags.make
CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o: ../using_the_mouse_for_annotation.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o -c "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/using_the_mouse_for_annotation.cpp"

CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/using_the_mouse_for_annotation.cpp" > CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.i

CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/using_the_mouse_for_annotation.cpp" -o CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.s

CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o.requires:

.PHONY : CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o.requires

CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o.provides: CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o.requires
	$(MAKE) -f CMakeFiles/using_the_mouse_for_annotation.dir/build.make CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o.provides.build
.PHONY : CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o.provides

CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o.provides.build: CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o


# Object files for target using_the_mouse_for_annotation
using_the_mouse_for_annotation_OBJECTS = \
"CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o"

# External object files for target using_the_mouse_for_annotation
using_the_mouse_for_annotation_EXTERNAL_OBJECTS =

using_the_mouse_for_annotation: CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o
using_the_mouse_for_annotation: CMakeFiles/using_the_mouse_for_annotation.dir/build.make
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_gapi.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_stitching.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_surface_matching.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_face.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_dnn_objdetect.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_structured_light.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_xobjdetect.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_fuzzy.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_line_descriptor.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_xphoto.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_hfs.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_stereo.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_reg.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_bgsegm.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_cvv.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_freetype.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_superres.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_quality.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_ccalib.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_sfm.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_aruco.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_bioinspired.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_img_hash.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_saliency.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_dpm.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_videostab.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_rgbd.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_xfeatures2d.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_hdf.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_phase_unwrapping.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_tracking.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_plot.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_datasets.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_text.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_dnn.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_optflow.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_ximgproc.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_ml.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_shape.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_objdetect.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_photo.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_video.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_calib3d.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_features2d.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_highgui.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_videoio.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_imgcodecs.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_imgproc.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_flann.so.4.1.0
using_the_mouse_for_annotation: /home/paulstein/installation/OpenCV-4.1.0/lib/libopencv_core.so.4.1.0
using_the_mouse_for_annotation: CMakeFiles/using_the_mouse_for_annotation.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable using_the_mouse_for_annotation"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/using_the_mouse_for_annotation.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/using_the_mouse_for_annotation.dir/build: using_the_mouse_for_annotation

.PHONY : CMakeFiles/using_the_mouse_for_annotation.dir/build

CMakeFiles/using_the_mouse_for_annotation.dir/requires: CMakeFiles/using_the_mouse_for_annotation.dir/using_the_mouse_for_annotation.cpp.o.requires

.PHONY : CMakeFiles/using_the_mouse_for_annotation.dir/requires

CMakeFiles/using_the_mouse_for_annotation.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/using_the_mouse_for_annotation.dir/cmake_clean.cmake
.PHONY : CMakeFiles/using_the_mouse_for_annotation.dir/clean

CMakeFiles/using_the_mouse_for_annotation.dir/depend:
	cd "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE" "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE" "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/build" "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/build" "/home/paulstein/opencv/Example_course/C++/WEEK 2/FIRST EXAMPLE/build/CMakeFiles/using_the_mouse_for_annotation.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/using_the_mouse_for_annotation.dir/depend

