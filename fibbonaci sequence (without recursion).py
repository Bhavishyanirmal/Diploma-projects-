n=int(input("enter numbers:"))
i=0
f1=0
f2=1
print(f1,f2,end=' ')

while i < n-2:
    f3=f1+f2
    print(f3,end=' ')
    f1=f2
    f2=f3
    i=i+1