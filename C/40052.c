#include <stdio.h>
#include <math.h>
int main(void)
{
    int flag, i, j, k, m, n;

    scanf("%d", &n);

	for(i=1;i<=n;i++){
		  scanf("%d",&m);
		  k=0;
		  for(j=2;j<=m/2;j++)
			     if(m%j==0)
					 k=1;
		  if(m!=1&&k==0||m==2||m==3)
			  printf("%d is a prime\n", m);
		  else
              printf("%d is'nt a prime\n", m);

	}
}