
#include <sys/types.h>
#include <unistd.h>
#include <cstdint>
#include <stdio.h>


int main()
{

	while(1)
	{
		printf ("My pid=%jd\n", (intmax_t) getpid ());
		printf ("Parent's pid=%jd\n", (intmax_t) getppid ());
	}

	return 0;
}
