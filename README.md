
# Automated-Attendance-System
Achievement

Hi there! , this project's aim is to detect ,recognize and mark attendance by face recognition but the project has a lot more objctives:

    + Detection
    + Recognition
    + Updating record in CSV files
    + Managing students data and faculty data through excel by the help of GUI
 
 
- Detection
Detection is done by the help of OpenCV and Haar cascades

Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. Today we will be using the face classifier. You can experiment with other classifiers as well.

- Recognition
Recognition is done by LBPH recogniser

Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.

LBPH is one of the easiest face recognition algorithms. It can represent local features in the images. It is possible to get great results (mainly in a controlled environment). It is robust against monotonic gray scale transformations. It is provided by the OpenCV library (Open Source Computer Vision Library).

- Manage attendance record in CSV files by GUI

- Managing students data through MySQL Database by the help of GUI


- Python libraries used
  + OpenCV-python
  + CSV
  + Numpy
  + Pillow
  + Tkcalenda
  + Time
  + datetime
  + tkinter
  +  MySQL-Connecter Python
