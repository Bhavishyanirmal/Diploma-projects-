n=int(input("Enter number:"))
i=2
count=0
while i<n:
	if n%i==0:
		count=count+1
	i=i+1
if count==0:
		print("this is prime number")
else:
		print("this is not prime")