public class Fibonacci{ 
	public static void main(String args[]){  
		int nums = fibonacci(8);  
		System.out.println(nums); 
	}    
static int fibonacci(int n){   
	if(n<=1) return 1;   
	return fibonacci(n-1)+fibonacci(n-2);   
} 
}