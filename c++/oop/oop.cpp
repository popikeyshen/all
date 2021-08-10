
/*
Here will be introduced in to 4 fundamental blocks of OOP in c++ example:
g++ oop.cpp -std=c++11
*/


#include <stdio.h>
#include <iostream>
using namespace std;

/// 1) Polymorphism example 
/// if we dont use polymorphism
/// output will be:
/// 18.84
/// 18.84
/// But real out is:
/// 18.84
/// 22.608
/// Because 3.5 will be converted to int 3

void calculate_circle_length(int radius)
{
	cout<<2*3.14*radius<<endl;
}
void calculate_circle_length(double radius)
{
	cout<<2*3.14*radius<<endl;
}

void polymorphism1()
{
	calculate_circle_length(3);
	calculate_circle_length(3.6);
}




class Animal
{
	private:

	public:
		string s="???";
		void say()
		{
			cout<<s<<endl;
		}
};

class Cat: public Animal
{
		string Cat::Animal::s="Meow";
};

class Dog: public Animal
{
		string s="Woof";
};


void polymorphism2()
{
	Cat cat;
	Dog dog;

	dog.say();
	cat.say();
}





int main()
{

polymorphism1();
polymorphism2();
return 0;
}
