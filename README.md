# Smile detector

This project based on open_cv library. It recognises smiles and tells how much the person smiled within a given time.

Follow this [guide](https://www.learnopencv.com/install-opencv3-on-macos/) for open_cv installation


Reference links:
http://pushbuttons.io/blog/2015/4/27/smile-detection-in-python-opencv
https://github.com/oarriaga/face_classification
http://flothesof.github.io/smile-recognition.html

## How to run

install opencv
`brew install opencv`

install virtual environment
`sudo pip install virtualenv virtualenvwrapper --ignore-installed six`

create new virtual environment
`mkvirtualenv opencv_env -p python`

activate the created virtual environment
`workon opencv_env`

install numpy
`pip install numpy`

link cv2
`cd ~/.virtualenvs/opencv_env/lib/python2.7/site-packages/`
`ln -s /usr/local/opt/opencv/lib/python2.7/site-packages/cv2.so cv2.so`
`cd ~ `

check that "/usr/local/Cellar/opencv/3.3.1_1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
and "/usr/local/Cellar/opencv/3.3.1_1/share/OpenCV/haarcascades/haarcascade_smile.xml" exist

run the program
`python smile_detector.py`

