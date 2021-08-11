
#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	int n=0;
	cout<< "Enter memory1 length:";
	cin>>n;
	// get memory
	char mem[n];

	cout<<"array created "<<sizeof(char)*n<<" bytes"<<endl;

// output
//Enter memory length:9000000
//Segmentation fault (core dumped)
//because stack length is less than 8mb
//to look max stack size: $ ulimit -a | grep stack


	cout<< "Enter memory2 length:";
	cin>>n;
	char *p_array = new char[n];
	if (p_array!=NULL)
	{
		cout<<"array created "<<sizeof( *p_array)*n<<" bytes"<<endl;
		// the size limit is 2147483647 bytes cause of int size

		for( int i=0; i<n; i++)
		{
			p_array[i]=1;
		}
		cout<<"q for quit ";
		cin>>n;
		//delete[] p_array;
	}
	else
	{ cout<<"too much"<<endl;}



	return 0;  //memory will be deleted here
}
