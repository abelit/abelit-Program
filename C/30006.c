#include <stdio.h>
int main(void)
{
    int i, mark;

    for(i = 1; i <= 5; i++){
        scanf("%d", &mark);
		if(mark>=60)
			 printf("Pass\n");
		else
			 printf("Fail\n");
	}}