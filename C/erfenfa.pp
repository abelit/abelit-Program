#include <stdio.h>
#include <math.h>

#define N 10000

double A,B,C;

double f(double x)
{
    return (A*x*x*x*x+B*x*x+C);
}

void BM(double a,double b,double eps1,double eps2)
{
    int k;
    double x,xe;
	double valuea = f(a);
	double valueb = f(b);
	if (valuea > 0 && valueb > 0 || valuea <0 && valueb < 0) return;

	printf("Finding root in the range: [%.3lf, %.3lf]\n", a, b);
    for(k=1;k<=N;k++) {
        x=(a+b)/2;
        xe=(b-a)/2;
        if(fabs(xe)<eps2 || fabs(f(x))<eps1) {
            printf("The x value is:%g\n",x);
            printf("f(x)=%g\n\n",f(x));
            return;
        }
        if(f(a)*f(x)<0) b=x;
        else a=x;
    }
    printf("No convergence!\n");
}

int main()
{
    double a,b,eps1,eps2,step,start;

    printf("Please input A,B,C:\n");
    scanf("%lf %lf %lf",&A,&B,&C);

    printf("Please input a,b, step, eps1,eps2:\n");
    scanf("%lf %lf %lf %lf %lf",&a,&b,&step,&eps1,&eps2);
    
	for (start=a; (start+step) <= b; start += step) {
		double left = start;
		double right = start + step;
		BM(left, right, eps1, eps2);
	}
    
    return 0;
}
