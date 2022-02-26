## Usage
The link to the code is: [Workshop Repository](https://github.com/mroe1234/workshops) it was devloped with following python version:
```
% python3 --version
Python 3.9.8
```
And the following libraries were used:
```
math
matplotlib
mpl_toolkits
numpy 
pylab 
```

### workshop1.py
```
% python3 workshop1.py -h
usage: workshop1.py [-h] [-s SHAPE] [-w]

Working with Trajectories

optional arguments:
  -h, --help            show this help message and exit
  -s SHAPE, --shape SHAPE
                        oval, flower or helix
  -w, --wind            enables wind disturbances
```
You can use -s to select the shape and -w to enable/disable wind.  Resultant graphs will appear on your screen when executed.
### trajectory.py
```
% python3 trajectory.py -h
usage: trajectory.py [-h] [-p PATH]

Working with Trajectories

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  line or spline
```
the -p parameter will determine if a polyline or spline solution is used.  Further, an mp4 file named `trajectory-{--path}` will be saved to your current directory showing the resultant path