
#include <algorithm>
#include <iostream>

bool gt(int x)
{
	return x>3;
}

using namespace std;
int main()
{
	// #include <algorithm>  - алгоритмы для контейнеров - последовательные, поиск, сортировка, соияния..


	vector<int> vec = {5,2,3,4,1};

	// min max
	cout<< "min " <<min(vec[0],vec[1])<<endl;
	cout<< "max " <<max(vec[0],vec[1])<<endl;

	// sort
	sort(begin(vec),end(vec));
	for(auto i:vec)
	{
		cout<<i<<endl;
	}


	// count if
	cout<< "count " << count_if(begin(vec),end(vec), gt)<<endl;

	int thr=3;
	// lambda functions
	cout<< "count lambda " <<count_if(begin(vec),end(vec), [thr](int x)
	{
		return x>thr;
	})<<endl;


	return 0;
}
