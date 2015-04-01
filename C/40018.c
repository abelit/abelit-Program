#include <stdio.h>
int main(void)
{
    int a, i, n, sn, tn;
    int ri, repeat;

    scanf("%d", &repeat);
    for(ri = 1; ri <= repeat; ri++){
        scanf("%ld%d", &a, &n);
		sn=0;
		tn=0;
		for(i=1;i<=n;i++){
			tn=tn*10+a;
			sn+=tn;
		}
      	printf("sum = %d\n", sn);
	}
}