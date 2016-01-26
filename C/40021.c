#include "stdio.h"
int main(void)
{
    int i, j, n;
    int repeat, ri;
    double e, product;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf("%d", &n);
		product=1;
		e=0;
		for(i=1;i<=n;i++){
			  product*=i;
              e+=(1/product);   
		}
		e+=1;
    	printf("e = %0.4f\n",e);
	}
}