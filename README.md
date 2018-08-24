# Spikes ComputerVision Framework

Spikes ComputerVision Framework, or scvf for short,
  is a framework that is made to make programming CV for the FRC easier
  
This framework wraps [opencv](www.opencv.org) and pipelines generated by [grip](https://wpiroboticsprojects.github.io/GRIP/#/)
in a way that is efficient and elegant.

Installation Instructions:

```
$ python3 -m pip install --index-url https://test.pypi.org/simple/ scvf
```
### API

use the ```pipeline_name``` key to send the pipeline_name <br/>
use the ```camera_id``` key to send the camera id <br/>
use the ```exposure``` key to send the exposure for the camera

### Notes

if you are using [grip](https://wpiroboticsprojects.github.io/GRIP/#/)
to generate your pipelines keep in mind that the pipelines generated from it
 aren't compatible with scf out of the box due to differences between python3 and python2
 
as of now, two changes are required:

1. change the enum for the [blur](https://docs.opencv.org/2.4/doc/tutorials/imgproc/gausian_median_blur_bilateral_filter/gausian_median_blur_bilateral_filter.html) type to a [python3-enum](https://docs.python.org/3/library/enum.html)
2. change the findContours function as instructed [here](https://stackoverflow.com/questions/25504964/opencv-python-valueerror-too-many-values-to-unpack)