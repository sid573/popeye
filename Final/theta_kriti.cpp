#include<bits/stdc++.h>
using namespace std;
#define PI 3.14159265
float distance(float x1, float y1, float x2, float y2) 
{ 
    // Calculating distance 
    return sqrt(pow(x2 - x1, 2) +  
                pow(y2 - y1, 2) * 1.0); 
} 
 

int main()
{
	float l1 = 28, l2 = 18; //Unit : cm
	l1 = 1058.2677165;
	l2 = 680.31496063;
	float x_center = 168.5,y_center = 300;

	float x,y,theta1,theta2,theta3;
	
	//fp = FILE *fp

	//fp = fopen('kriti.txt','r+');
	ifstream inFile;
	std::ifstream infile("kriti.txt");
	inFile.open("kriti.txt");


	while (infile >> x >> y)
	{
    	
		x = x - x_center;
		y = y - y_center;

		float l = distance(x,y,x_center,y_center);
		cout<<"Vector Distance in Pixels "<<l<<endl;

		theta2 = (acos(((l1*l1) + (l2*l2) - (l*l))/(2 * l1 * l2))) * (180/PI);
		theta1 = (acos(((l1*l1) + (l*l) - (l2*l2))/(2 * l1 * l))) * (180/PI);
		
		cout<<(((l1*l1) + (l2*l2) - (l*l))/(2 * l1 * l2))<<endl;

		float y_dist = x - x_center;
		float x_dist = y - y_center;

		theta3 = atan((float)y_dist /(float) x_dist);
		theta3 *= (180/PI);

		cout<<"Theta1 "<<theta1<<endl;
		cout<<"Theta2 "<<theta2<<endl;
		cout<<"Theta3 "<<theta3<<endl;

	}
	
	

}
