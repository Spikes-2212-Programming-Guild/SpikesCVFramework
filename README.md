# Spikes ComputerVision Framework

Spikes ComputerVision Framework, or scvf for short,
  is a framework that is made to make programming CV for the FRC easier
  
This framework wraps [opencv](www.opencv.org) and pipelines generated by [grip](https://wpiroboticsprojects.github.io/GRIP/#/)
in a way that is efficient and elegant.

Installation Instructions:

```
$ python3 -m pip install scvf
```
## API

#### communication through network tables
use the ```pipeline_name``` key to send the pipeline_name <br/>
use the ```camera_id``` key to send the camera id <br/>
use the ```exposure``` key to send the exposure for the camera

#### pipeline compatibility
Though we recommend grip as the main tool to generate cv2 pipelines
using grip is not strictly required <br/>
You can provide any object to server as a pipeline as long as it contains the next two methods: <br>
```process()``` - a method that processes a given image <br/>
```get_output()``` - a method that returns the output of the processing

#### IO functions 
scvf receives two functions that are responsible for communications with external data sources. <br/>
1. ```settings_supplier(callback)``` this function receives settings and supplies them to callback provided to it.
2. ```output_consumer(output)``` this function sends the output of the image processing to it's next destination
## Notes

#### GRIP and SCVF compatibility
if you are using [grip](https://wpiroboticsprojects.github.io/GRIP/#/)
to generate your pipelines keep in mind that the pipelines generated from it
 aren't compatible with scvf out of the box due to differences between python3 and python2
 
as of now, these changes are required:

* change the enum for the [blur](https://docs.opencv.org/2.4/doc/tutorials/imgproc/gausian_median_blur_bilateral_filter/gausian_median_blur_bilateral_filter.html) type to a [python3-enum](https://docs.python.org/3/library/enum.html)
* change the findContours function as instructed [here](https://stackoverflow.com/questions/25504964/opencv-python-valueerror-too-many-values-to-unpack)
* add a ```get_output()``` method that is compatible with the API specified above

#### IO implementations
* make sure that your custom ```output_consumer``` is compatible with the output provided by your pipelines.
