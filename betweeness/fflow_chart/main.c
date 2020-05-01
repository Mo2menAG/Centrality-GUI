#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {


    int a, b  ;
    int mul =0  , i;

	printf(" 5ra " );
		scanf("%d", &a )  ;
	printf(" 5ra " );
		scanf("%d",&b)  ;
		/*a=a-'0';
		b=b-'0';*/
		    printf(" mul is %d \n",mul);
		    printf(" a is %d \n ",a);
	for(i=0;i<8;i+=1)
	{
		if(b%2!=0)
		{
		    printf(" mul is %d \n",mul);
		    printf(" a is %d \n ",a);
		    mul+=(a<<i);
		}
		b=b>>1;
	}





	printf(" mul = %d \n" ,mul );
	printf(" a = %d \n" ,a );
	printf(" b = %d \n" ,b );

	return 0;
}
