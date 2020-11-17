## DoIKnowYou

DoIKnowYou (DIKY) is an implementation of a Face Recognition framework using Haar Cascade classifiers inspired from the CVPR 2001 paper by Viola-Jones that can handle multiple client verification requests on a server using Multithreading and Synchronisation Policies.

Dependencies
------------

The following libraries are needed:

* OpenCV 4.4.0 

On Ubuntu 20.04, you can install with: `pip install opencv-contrib-python`

Please check dependencies and proceed. For maximal performance you can build from source with CUDA support.

* Python 3.8.3

* Python packages (newer packages will likely work, though these are the exact versions that we used):
```
      numpy>=1.17.3
      socket
      tqdm
      threading
```
Setting up a virtual environment like `virtualenv`  will help keep your Python environment safe. We recommend installing all dependencies using this.

Running
-------

##### Basic usage:

There are two important files, `Client.py` and `Thread_Server.py` and their dependency files. Fork and clone this repository in your local machine. Open one terminal to run the `Thread_Server.py` and open multiple terminals for each instance of `Client.py` using:
``` console
python3 client.py
```
``` console
python3 server.py
```
In the client side, a `Enter your name` prompt will come and upon entering, a virtual terminal will be created. The server side will bind to localhost:5000 after launching. If the port is busy, please change the port address in both client and server side. 
* If a log comes, `[RDY] Socket is now Deployed`, we are now ready to listen for client requests. Else restart the program.

##### Commands on server

To listen for client requests, use
```console
listen
```

To register a new user using a video, use
```console
trainVideo
```

A prompt will appear asking for video location, enter the absolute/relative address of the video. A consequent prompt will appear, asking to annotate the video with the name of the person.

To register a new user using a webcam, use
```console
trainWebc
```
A prompt will appear, asking to annotate the video with the name of the person.

To quit, use
```console
quit
```

##### Commands on client

To send a verification request using a video, use
```console
video
```

A prompt will appear asking for video location, enter the absolute/relative address of the video. A consequent prompt will appear, asking to annotate the video with the name of the person. After this a window will open up, showing the video and the detected person.

To register a new user using a webcam, use
```console
webcam
```

To quit, use
```console
quit
```
To avoid unexpected killed threads and orphaned processes, **do not use** this command in between client requests. System may experience a lag and you might have to hard-reboot. *You have been warned.*

### Some flex :wink:
After login on Server:
![Server Login](Assets/server_login.png)

After login on a Client:
![Client Login](Assets/client_login.png)

A 4 client request session to showcase Multithreading:
![multi_thread_req](Assets/request1.png)

### Dataset

We have trained face recognition on two videos of actors Will Smith and Emma Watson, because we are in *The Pursuit of Happyness* and *Hermione Granger* is :two_hearts: The videos are provided in the ```videos``` folder for retraining. Feel free to add more and go wild.

### References
*Note: You need IEEE Access for accessing these papers. We strongly discourage pirated websites. Please support the research community.*
* [P. Viola and M. Jones, "Rapid object detection using a boosted cascade of simple features," Proceedings of the 2001 IEEE Computer Society Conference on Computer Vision and Pattern Recognition. CVPR 2001, Kauai, HI, USA, 2001, pp. I-I, doi: 10.1109/CVPR.2001.990517.](https://ieeexplore.ieee.org/document/990517)
* [*RGB-H-CbCr Skin Colour Model for Human Face Detection*, Nusirwan Anwar bin Abdul Rahman et al., Faculty of Information Technology, Multimedia University.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.718.1964&rep=rep1&type=pdf)
* [L. Cuimei, Q. Zhiliang, J. Nan and W. Jianhua, "Human face detection algorithm via Haar cascade classifier combined with three additional classifiers," 2017 13th IEEE International Conference on Electronic Measurement & Instruments (ICEMI), Yangzhou, 2017, pp. 483-487, doi: 10.1109/ICEMI.2017.8265863.](https://ieeexplore.ieee.org/document/8265863)
