#include <stdio.h>
int main(void)
{
    long sum;
    sum=0;
    int i=1;
    int count=0;

    printf("Enter the number of integers you want to sum:");
    scanf("%d",&count);
    
    while(i<=count)
    {
      sum += i++;
    }
    printf("Total of the first %d numbers is %d\n",count,sum);
    return 0;
}
