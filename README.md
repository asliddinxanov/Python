## Imgae Processing in Python

Images define the world, each image has its own story, it contains a lot of crucial information that can be useful in many ways. This information can be obtained with the help of the technique known as Image Processing.

It is the core part of computer vision which plays a crucial role in many real-world examples like robotics, self-driving cars, and object detection. Image processing allows us to transform and manipulate thousands of images at a time and extract useful insights from them. It has a wide range of applications in almost every field. 

Python is one of the widely used programming languages for this purpose. Its amazing libraries and tools help in achieving the task of image processing very efficiently. 

## What is image processing?
As the name says, image processing means processing the image and this may include many different techniques until we reach our goal.

The final output can be either in the form of an image or a corresponding feature of that image. This can be used for further analysis and decision making.

But what is an image?

An image can be represented as a 2D function F(x,y) where x and y are spatial coordinates. The amplitude of F at a particular value of x,y is known as the intensity of an image at that point. If x,y, and the amplitude value is finite then we call it a digital image. It is an array of pixels arranged in columns and rows. Pixels are the elements of an image that contain information about intensity and color. An image can also be represented in 3D where x,y, and z become spatial coordinates. Pixels are arranged in the form of a matrix. This is known as an `RGB` image.

###### There are various types of images:

・RGB image: It contains three layers of 2D image, these layers are Red, Green, and Blue channels.

・Grayscale image: These images contain shades of black and white and contain only a single channel.

## Classic image processing algorithms
### 1. Morphological Image Processing
Morphological image processing tries to remove the imperfections from the binary images because binary regions produced by simple thresholding can be distorted by noise. It also helps in smoothing the image using opening and closing operations.

Morphological operations can be extended to grayscale images. It consists of non-linear operations related to the structure of features of an image. It depends on the related ordering of pixels but on their numerical values. This technique analyzes an image using a small template known as structuring element which is placed on different possible locations in the image and is compared with the corresponding neighbourhood pixels. A structuring element is a small matrix with 0 and 1 values.

### 2. Gaussian Image Processing
Gaussian blur which is also known as gaussian smoothing, is the result of blurring an image by a Gaussian function.

It is used to reduce image noise and reduce details. The visual effect of this blurring technique is similar to looking at an image through the translucent screen. It is sometimes used in computer vision for image enhancement at different scales or as a data augmentation technique in deep learning.

### 3. Fourier Transform in image processing
Fourier transform breaks down an image into sine and cosine components. 

It has multiple applications like image reconstruction, image compression, or image filtering. 

Since we are talking about images, we will take discrete fourier transform into consideration.

Let’s consider a sinusoid, it comprises of three things:

・Magnitude – related to contrast 
・Spatial frequency – related to brightness
・Phase – related to color information

### 5. Wavelet Image Processing

We saw a Fourier transform but it is only limited to the frequency. Wavelets take both time and frequency into the consideration. This transform is apt for non-stationary signals. 

We know that edges are one of the important parts of the image, while applying the traditional filters it’s been noticed that noise gets removed but image gets blurry. The wavelet transform is designed in such a way that we get good frequency resolution for low frequency components.
