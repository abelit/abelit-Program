#include "stdio.h"
#include "math.h"
int main(void)
{int count, i, j, k, m, n;
    int ri,repeat;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat;ri++){
        scanf("%d%d", &m, &n);
		count=0;
	    printf("primes:\n");
		for(i=m;i<=n;i++){
			k=1;
			for(j=2;j<=i/2;j++){
				if(i%j==0){
					k=0;
					break;
				}
			}
			if(k==1&&i!=1){
				printf("%d ",i);
				if((++count)==6){
				    count=0;   
					printf("\n");
				}
			}
		}
	    printf("\n");
	}
}