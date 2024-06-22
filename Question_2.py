f1=1
f0=0
n=int(input("Enter the value of n: "))
print(f0,f1,end=" ")
for i in range(0,n-1):
    fib=f0+f1
    f0=f1
    f1=fib
    print(fib,end=" ")
