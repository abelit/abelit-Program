#include <stdio.h>
int main(void)
{
    int repeat, ri;
    double rate, salary, tax;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf("%lf", &salary);
        if(salary <=850)
			rate=0;
		else if(salary<=1350 )
                 rate=0.05;
		else if(salary<=2850)
			      rate=0.1;
		else if(salary<=5850)
			      rate=0.15;
		else 
			  rate=0.2;
		tax = rate*(salary - 850);
        printf("tax = %0.2f\n", tax);
	}
}