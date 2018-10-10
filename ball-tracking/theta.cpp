#include<bits/stdc++.h>
using namespace std;
#define PI 3.14159265
int main()
{
	float x_center,y_center;
	float x_ref = 0,y_ref = 0;
	cin>>x_center>>y_center;

	
	float x,y; //Balloon
	cin>>x>>y;
	float y_dist = x - x_center;
	float x_dist = y - y_center;

	float theta = atan((float)y_dist /(float) x_dist);
	theta*=(180/PI);
	cout<<theta<<endl;
}
