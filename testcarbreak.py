/******************************************************************************
* Author : Aaksha Jaywant & Atharv Desai                                      *
* RTES Project : Autonomous Car Braking System                                *
* Reference: https://www.geeksforgeeks.org/opencv-c-program-face-detection/   *
******************************************************************************/



#include "object_detection.h"

extern sem_t sem_obj;
uint8_t motor_STOP_flag = 0;
using namespace std; 
using namespace cv; 

string casN, nestedCasN;
CascadeClassifier casC, nestedcasN;
Mat obj_frame;
VideoCapture capture;


double scale = 1;

int objdetect_action(Mat& img, CascadeClassifier& cascade, double scale)
{
	int ret;
	Mat gray_image;
	Mat resize_image;
	vector<Rect> stop_sign;
	int radius; 
	/**** Converting RGB image to grayscale Image ******/
	cvtColor(img,gray_image,COLOR_BGR2GRAY);                   	
	double fx = 1/scale;
	resize(gray_image,resize_image,Size(),fx,fx,INTER_LINEAR);	
	
    /***** equalizes the histogram for grayscale image by calculating, normalizing and computing the integral of histrogram ******/
	equalizeHist(resize_image,resize_image);
    /***** detects the stop sign of different size in the image and returns as a list of rectangles ********/
	cascade.detectMultiScale(resize_image,stop_sign,1.1,2,0|CASCADE_SCALE_IMAGE,Size(30,30)); 
	for (size_t i = 0;i < stop_sign.size();i++) 
    	{ 
        	Rect r = stop_sign[i]; 
        	Mat resize_imageROI; 
        	Point center; 
        	Scalar color = Scalar(255, 0, 0); // Color for Drawing tool 
        	
  
        	double aspect_ratio = (double)r.width/r.height; 
        	if(0.75 < aspect_ratio && aspect_ratio < 1.3) 
        	{ 
            		center.x = cvRound((r.x + r.width*0.5)*scale); 
            		center.y = cvRound((r.y + r.height*0.5)*scale); 
            		radius = cvRound((r.width + r.height)*0.25*scale); 
            		circle(img,center,radius,color,3,8,0); 
        	} 
        	else
		{
            		rectangle(img,cvPoint(cvRound(r.x*scale),cvRound(r.y*scale)),cvPoint(cvRound((r.x + r.width-1)*scale),
			cvRound((r.y + r.height-1)*scale)),color,3,8,0);
		} 
	}
	
		namedWindow("OUTPUT_SIGN",CV_WINDOW_NORMAL); 
		cvResizeWindow("OUTPUT_SIGN",800,800);
		imshow("OUTPUT_SIGN",img); 

		ret = (stop_sign.size() > 0) ? radius : 15;	// If radius of circle > 15 then the sign detected
		return ret;

}



void *objdetect_thread(void *args)
{
	long int count = 0;
	static double start = 0.0;
   	static double stop   = 0.0;
   	static double wcet  = 0.0;
	int ret_obj;
	
	/**** camera object detection init *****/
	casC.load("/home/pi/opencv-4.2.0/data/haarcascades/stopstop.xml");   	
	/****** To start a video : If 0 --> then from camera ; If 1 --> then from a saved video ******/
	capture.open(0);	

	
	for(;;)
	{
		sem_wait(&sem_obj);
		start = timestamp();		
		capture >> obj_frame;
		if( obj_frame.empty() ) 
                	break; 
            	Mat obj_frame1 = obj_frame.clone();
		ret_obj = objdetect_action(obj_frame1,casC,scale);
		if(ret_obj > 15)   // Based on returned value from objdetect_action function,flag set/reset for motor
		{
			motor_STOP_flag = 1;
		}
		else
		{
			motor_STOP_flag = 0;
		}
		
		stop = timestamp();		
		if ( ( stop - start ) > wcet )
      		{
         		wcet = stop - start;
		}
		 syslog(LOG_DEBUG, "object detection Service WCET: %.4f \n", wcet );	
	}
}
