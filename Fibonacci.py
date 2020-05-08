n=int(input("enter the no of terms required in fibonacci series"))
a=0
b=1
if n<=0:
	print(" the series is:",a)
else:
	print("The fibonacci series is:")
	print(a,b,end=" ")
	for i in range(2,n):
	        c=a+b
	        print(c,end=" ")
        	a=b
        	b=c
