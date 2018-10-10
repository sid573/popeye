from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
	help="path to the (optional) image file")

args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
redLower = (17, 15, 100)
redUpper = (50, 56, 200)
blueLower = (86, 31, 4)
blueUpper = (220, 88, 50)
yellowLower = (25, 146, 190)
yellowUpper = (62, 174, 250)

img = cv2.imread(args["image"]);

img = imutils.resize(img,width = 600)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, greenLower, greenUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)


cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
center = None

if len(cnts) > 0:
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

	if radius > 10:
		cv2.circle(img, (int(x), int(y)), int(radius),
			(0, 255, 255), 2)
		cv2.circle(img, center, 5, (0, 0, 255), -1)


mask = cv2.inRange(hsv, redLower, redUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
center = None

if len(cnts) > 0:
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

	if radius > 10:
		cv2.circle(img, (int(x), int(y)), int(radius),
			(0, 255, 255), 2)
		cv2.circle(img, center, 5, (0, 0, 255), -1)

mask = cv2.inRange(hsv, blueLower, blueUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
center = None

if len(cnts) > 0:
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

	if radius > 10:
		cv2.circle(img, (int(x), int(y)), int(radius),
			(0, 255, 255), 2)
		cv2.circle(img, center, 5, (0, 0, 255), -1)


mask = cv2.inRange(hsv, yellowLower, yellowUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
center = None

if len(cnts) > 0:
	c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

	if radius > 10:
		cv2.circle(img, (int(x), int(y)), int(radius),
			(0, 255, 255), 2)
		cv2.circle(img, center, 5, (0, 0, 255), -1)

cv2.imshow("image",img)
cv2.waitKey(0);
time.sleep(2.0)

cv2.destroyAllWindows()





