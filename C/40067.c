#include "stdio.h"
int main(void)
{
     int i, j, n;
    int repeat, ri;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat; ri++){
         scanf("%d", &n);
		 for(i=0;i<2*n-1;i++){
			 int temp=(i<2*n-2-i)?i:2*n-2-i;
			 int blank=(n-(temp+1))*2;
			 for(j=1;j<=blank;j++)
				 printf(" ");
			 temp=temp*2+1;
			 for(j=1;j<=temp;j++)
				 if(j<temp)
				 printf("* ");
				 else
					 printf("*");
			 printf("\n");
		 }
	}}