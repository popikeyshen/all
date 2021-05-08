#include <map>
#include <set>
#include <iostream>

using namespace std;
int main()
{

	//множества #include <set>
	//гарантируется сортировка и уникальность
	set<string> mn;
	mn.insert("viacheslav");
	for(auto x : mn)		// for based loop  'g++ c++.cpp -std=c++11'
	{
		std::cout<<x<<std::endl;
	}
	mn.erase("viacheslav");
	std::cout<<mn.size()<<std::endl;

	return 0;
}
