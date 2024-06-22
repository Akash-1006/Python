a=int(input("Enter A: "))
b= int(input("Enter B: "))
for i in range(a+1,b):
    if(i%2==0 or i%3==0 or i%5==0 or i%7==0):
        print(i,end=",")
    else:
        continue
        
