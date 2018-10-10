import math
import numpy as np
def distance(x1,y1,x2,y2):

	return math.sqrt(((x2-x1) ** 2) + ((y2 - y1) ** 2))

def get_theta(x,y):
	""" theta """
	PI = 3.14159265
	l1 = 1058.2677165
	l2 = 680.31496063
	x_center = 168.5
	y_center = 300

	x = x - x_center
	y = y - y_center

	l = distance(x,y,x_center,y_center)
	print("Distance : " + str(l))

	theta2 = (np.arccos(((l1*l1) + (l2*l2) - (l*l))/(2 * l1 * l2))) * (180 / PI)
	theta1 = (np.arccos(((l1*l1) + (l*l) - (l2*l2))/(2 * l1 * l))) * (180/PI);

	y_dist = y - y_center
	x_dist = x - x_center

	theta3 = np.arctan(y_dist / x_dist);
	theta3 = theta3 * (180/PI)

	print("theta1 " + str(theta1))
	print("theta2 " + str(theta2))
	print("theta3 " + str(theta3))

	return theta1,theta2,theta3

