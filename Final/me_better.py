#python color_tracking.py --video balls.mp4
#python color_tracking.py
 
# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import time
import urllib #for reading image from URL
import theta as theta
 
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
ap.add_argument("-i","--image",help = "path to image")
args = vars(ap.parse_args())
 
# define the lower and upper boundaries of the colors in the HSV color space
#lower = {'red':(166, 84, 141), 'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119), 'orange':(0, 50, 80)} #assign new item lower['blue'] = (93, 10, 0)
#upper = {'red':(186,255,255), 'green':(86,255,255), 'blue':(117,255,255), 'yellow':(54,255,255), 'orange':(20,255,255)}

lower = {'red':(0, 154, 130), 'green':(48,48,56), 'blue':(98,37,53), 'yellow':(23, 59, 119)} #assign new item lower['blue'] = (93, 10, 0)
upper = {'red':(186,204,187), 'green':(93,154,138), 'blue':(124,185,113), 'yellow':(54,255,255)}

 
# define standard colors for circle around the object
colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217)}
 
#pts = deque(maxlen=args["buffer"])
 
# if a video path was not supplied, grab the reference
# to the webcam\

flag_for_image = 0;

if args.get("image"):
    image = cv2.imread(args["image"])
    flag_for_image = 1;
elif args.get("video"):
    cv2.VideoCapture(args["video"])
else:
    cv2.VideoCapture(1)


theta_red = []
theta_blue = []
theta_green = []
theta_yellow = []

# keep looping

if(flag_for_image == 0):
    while True:
        # grab the current frame
        (grabbed, frame) = camera.read()
        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if args.get("video") and not grabbed:
            break
     
        #IP webcam image stream
        #URL = 'http://10.254.254.102:8080/shot.jpg'
        #urllib.urlretrieve(URL, 'shot1.jpg')
        #frame = cv2.imread('shot1.jpg')
     
     
        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = imutils.resize(frame, width=600)
        
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        #for each color in dictionary check object in frame
        for key, value in upper.items():
            # construct a mask for the color from dictionary`1, then perform
            # a series of dilations and erosions to remove any small
            # blobs left in the mask
            kernel = np.ones((9,9),np.uint8)
            mask = cv2.inRange(hsv, lower[key], upper[key])
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                   
            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None
           
            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
           
                # only proceed if the radius meets a minimum size. Correct this value for your obect's size
                if radius > 0.5:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                    cv2.putText(frame,key + " ball", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
     
         
        # show the frame to our screen
        cv2.imshow("Frame", frame)
       
        key = cv2.waitKey(1) & 0xFF
        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break

else:

    image = imutils.resize(image,width = 600)
    #blurred = cv2.GaussianBlur(image, (11, 11), 0)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    for key, value in upper.items():
            # construct a mask for the color from dictionary`1, then perform
            # a series of dilations and erosions to remove any small
            # blobs left in the mask
            kernel = np.ones((9,9),np.uint8)
            mask = cv2.inRange(hsv, lower[key], upper[key])
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                   
            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None
           
            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
           
                # only proceed if the radius meets a minimum size. Correct this value for your obect's size
                if radius > 0.5:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
	                cv2.circle(image, (int(x), int(y)), int(radius), colors[key], 2)
	                cv2.putText(image,key + " ball", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
	                
	                x,y = center

	                print(str(key) + "Balloon : ",end=" ")
	                print(center);

	                theta1,theta2,theta3 = theta.get_theta(x,y)

	                if(key == 'red'):
	                	theta_red = [theta1,theta2,theta3,y]
	                elif(key == 'green'):
	                	theta_green = [theta1,theta2,theta3,y]
	                elif(key == 'blue'):
	                	theta_blue = [theta1,theta2,theta3,y]
	                elif(key == 'yellow'):
	                	theta_yellow = [theta1,theta2,theta3,y]

	                #RBGY
	                if(key == 'red'):
		                f = open("kriti_2.txt","w")
		                f.write(str(theta_red[0]) + "," + str(theta_red[1]) + "," + str(theta_red[2]) + "," + str(theta_red[3]))

	                #print(str(theta1) + " " + str(theta2) + " " + str(theta3))

					#f = open("myfile.txt", "w")
					#f.write(str(center))

    # show the frame to our screen



    cv2.imshow("image", image)
    print(image.shape)
    key = cv2.waitKey(0)
    time.sleep(1)
    


# cleanup the camera and close any open windows
#camera.release()
cv2.destroyAllWindows()
