#include <stdio.h>
#include<math.h>
int main(void)
{
    int count, in, sum;
    int repeat, ri;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat; ri++){
        count=sum=0;
		scanf("%d", &in);
		do{
			 count++;
			 sum+=labs(in%10);
		}while((in/=10)!=0);
    	printf("count = %d, sum = %d\n", count, sum);
	}
}