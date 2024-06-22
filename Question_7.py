a=input("Enter Date:")
b=a[6:10]
n=int(b)
flag=False
if(n%4==0 or n%400==0 and n%100!=0):
    print("Leap Year")
    flag=True
else:
    print("Not a Leap Year")
    flag=False
def Leapy(n):
    if(not(n%4==0 and n%400==0 or n%100!=0)):
        Leapy(n+1)
    else:
        return n
def Leapn(n):
    if((n%4==0 and n%400==0 or n%100!=0)):
        return n
    else:
        Leapn(n-1)
if(flag):
    L=Leapy(n+1)
else:
    L=Leapn(n-1)
print("Anniversary Date:04/11/",L)
