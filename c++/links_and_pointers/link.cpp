

#include <stdio.h>
#include <iostream>
using namespace std;


void example1()
{
	int x=1;
	int &y = x;
	int z = y;

	cout<<x<<" "<<y<<" "<<z<<endl;
	x=2;
	cout<<x<<" "<<y<<" "<<z<<endl;

// output
// 1 1 1
// 2 2 1
// because y will be the same momory block as x
}

void example2()
{
	int x=1;
	int *y = &x;
	int z = *y;

	cout<<x<<" "<<*y<<" "<<z<<endl;
	x=2;
	cout<<x<<" "<<*y<<" "<<z<<endl;

// output
// 1 1 1
// 2 2 1
// because y will be the same momory block as x
}

void example3()
{
	int x;
	cout<< sizeof(x)<< " " << sizeof(&x)<<endl;

// size of int in 64x system is 8 byte
}

int main()
{
example1();
example2();
example3();
return 0;
}



