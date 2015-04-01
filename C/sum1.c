#include <stdio.h>
int main(void)
{
    int i,sum,count;
    sum=0;
    printf("Enter the last number that you want to sum:\n");
    scanf("%d",&count);
    for(i=0;i<=count;i++)
    {
         sum=sum+i;
    }
    printf("1+2+...+99+100=%d\n",sum);
}
