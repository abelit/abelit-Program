#include <stdio.h>
int main(void)
{
    int i, n;
    int repeat, ri;
    double distance, height;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf("%lf%d", &height, &n);
		distance=0;
		for(i=1;i<=n;i++){
			   if(i==1)
                   distance+=height;
			   else
				   distance+=(2*height);
			   height/=2;
		}
      	printf("distance = %.1f, height = %.1f\n", distance, height);
	}
}