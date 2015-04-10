#define N 10
float f(float x)
{
	float y;
	y=1/(1+x*x);
	return y;
}

main()
{
	int i;
	float h=0.1,s,x0,x1,x2;
	float x[N+1];
	for(i=0;i<=N;i++)
	{
		x[i]=i*h;
	}
	printf("Please input x:");
	scanf("%f",&x0);
	s=f(x[N-1])+(x0-x[N-1]/f(x[N]));
	for(i=N-2;i>=0;i--)
	{
		s=f(x[i])+(x0-x[i])/s;
	}
	printf("The result is:%f\n",s);
}