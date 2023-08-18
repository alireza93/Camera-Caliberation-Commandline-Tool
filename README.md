# Camera Calibration Commandline Tool
A simple commandline script to perform camera calibration using a series of control images containing a chequered pattern.  
## How to use
Requires OpenCV to run. The command will look like this:
```
python CalibrateCamera.py "path/to/image/folder/" pw ph
```
### Arguments
- The first argument is the path pointing to the folder containing the control images. This can be a relative path to the location of the code. 
- **pw:** width of the pattern
- **ph:** height of the pattern
### Outputs 
The quality of the calibration can be judged by the value of the *re-projection error* given as the first output. A value of around $1$ or lower is desirable.

If the calibration is successful the code will print out the intrinsic camera parameters: the *camera matrix* and the *distortion coefficient*. In addition, for each image, it gives a *rotation vector* and a *translation vector*.
