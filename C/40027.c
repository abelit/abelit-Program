#include <stdio.h>
int main(void)
{
    int digit, in, power, temp;
    int repeat, ri;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf("%d", &in);
        if(in<0)
			in=-in;
		power=0;
		temp=0;
		do{
           power++;
		   temp=temp*10+in%10;
		}while((in/=10)!=0);
       
		while(power>0){
              digit=temp%10;
			  printf("%-2d", digit);
			  temp/=10;
              power--; 
		}
     	printf("\n");
	}
}