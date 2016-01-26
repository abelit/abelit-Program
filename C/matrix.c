#define M 4
#define N 3
#define P 2
main()
{
	int i,j,k;
	int a[M+1][N+1],b[N+1][P+1],c[M+1][P+1];
	printf("Please input matrix A:\n");
	for(i=1;i<=M;i++)
	{
		for(j=1;j<=N;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	printf("Please input matrix B:\n");
	for(i=1;i<=N;i++)
	{
		for(j=1;j<=P;j++)
		{
			scanf("%d",&b[i][j]);
		}
	}
	for(i=1;i<=M;i++)
	{
		for(j=1;j<=P;j++)
		{
			c[i][j]=0;
			for(k=1;k<=N;k++)
			{
				c[i][j]=c[i][j]+a[i][k]*b[k][j];
			}
		}
	}
	printf("The value of matrix C:\n");
	for(i=1;i<=M;i++)
	{
		for(j=1;j<=P;j++)
		{
			printf("%d ",c[i][j]);
		}
		printf("\n");
	}
	getchar();
}