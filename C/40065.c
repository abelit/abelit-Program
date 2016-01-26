#include "stdio.h"
#include "math.h"
int prime(int n);
int main(void)
{
    int i, m;
    int repeat, ri;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf("%d", &m);
        printf("%d = ", m);
		for(i=2;i<=m/2;i++){
			while(prime(m)==0&&prime(i)!=0&&m%i==0){
				  printf("%d*", i);
				  m=m/i;  /*m/=i;*/
			}
		}
        printf("%d\n", m);
    }
}


int prime(int n){
	int  t;
	if(n==1)
		return 0;
	for(t=2;t<=n/2;t++)
		if(n%t==0)
			return 0;
    return 1;
}