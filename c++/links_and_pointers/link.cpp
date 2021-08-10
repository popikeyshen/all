

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


void example4()
{
	int x=1;
	int *p = &x;
	int **pp = &p;
	int ***ppp = &pp;

	***ppp=2;
	cout<<x<<endl;
	//x=2
}

void example5()
{
	int a=1;
	int b=2;
	int c=3;	

	int *p = &a;
	
	cout<<*(p)<<endl;
	cout<<*(p+1)<<endl;
	cout<<*(p+2)<<endl;


	cout<<*(p+3)<<endl;
	cout<<*(p+10)<<endl;
	cout<<*(p+20)<<endl;

	// output:
	// 1
	// 2
	// 3
	// -298155644
	// ...
	// cout<<*(p+20000)<<endl;
	// segmentation falut error 
	// #include <signal.h>  https://habr.com/ru/post/131412/

}


void example6()
{
	int a[5]={1,2,3,4,5};
	int *p = a;
	int *q = a+3;

	cout << "a\t" 		<<a	<<endl;
	cout << "&a[0]\t"	<<&a[0]	<<endl;
	cout << "&a[1]\t"	<<&a[1]	<<endl;
	cout << "a[0]\t"	<<a[0]	<<endl;
	cout << "q-p\t"		<< q-p	<<endl;

//a	0x7fff9de481c0
//&a[0]	0x7fff9de481c0
//&a[1]	0x7ffd8ea98bb4
//a[0]	1
//q-p	3   //result is not number of bytes - result is number of int's

}

int main()
{
	cout<<"example1"<<endl;
	example1();
	cout<<"example2"<<endl;
	example2();
	cout<<"example3"<<endl;
	example3();
	cout<<"example4"<<endl;
	example4();
	cout<<"example5"<<endl;
	example5();
	cout<<"example6"<<endl;
	example6();

	return 0;
}



