#include "stdio.h"
int main(void)
{
    int i, digit, m, n, number, sum;
    int repeat, ri;

    scanf("%d",&repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf("%d%d", &m, &n);
        printf("result:\n");
		for(i=m;i<=n;i++){
			 number=i;
			 sum=0;
			 do{
				 sum+=(number%10)*(number%10)*(number%10);

			 }while((number/=10)!=0);
			 if(sum==i)
				 printf("%d\n",i);
		}
	}
}