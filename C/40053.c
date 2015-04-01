#include <stdio.h>
int main(void)
{
    int digit, x;
    int repeat, ri;

    scanf("%d",&repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf ("%d", &x);
/*---------*/
		if(x<0)
			x*=-1;
		do{
			digit=x%10;
			printf("%d ", digit);

		}while((x/=10)!=0);
    	printf("\n");
	}
}