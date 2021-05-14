#include <map>
#include <set>
#include <iostream>

using namespace std;
int main()
{
	// асоциативные контейнеры set, map

	//множества #include <set>
	//гарантируется сортировка и уникальность, быстрый поиск
	set<string> mn = {"Vova", "Ania", "Vova"};
	mn.insert("viacheslav");
	for(auto x : mn)		// for based loop  'g++ c++.cpp -std=c++11'
	{
		cout<<x<<endl;   //Ania Vova viacheslav
	}
	mn.erase("viacheslav");
	cout<<mn.size()<<endl;
	cout<< mn.count("Ania") <<endl;

	map< vector<string>, int > m;
	vector<string> stations;
	//m[stations]=n;
	cout<<m.size();

	return 0;
}
