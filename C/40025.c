#include <stdio.h>
int main(void)
{
    int factor, m, n, number, sum;
    int repeat, ri;

    scanf("%d",&repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf("%d%d", &m, &n);
        printf("result:\n");
		for(number=m;number<=n;number++){
			   sum=0;
			   for(factor=1;factor<=number/2;factor++)
				      if(number%factor==0)
					        sum+=factor; 			      
			   if(number==sum||number==1){
			      printf("%d = 1", number);
				  for(factor=2;factor<=number/2;factor++)
				      if(number%factor==0)
                             printf(" + %d", factor);
                  printf("\n");
  
			   }
		}
	}
}