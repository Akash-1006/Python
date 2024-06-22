try:
    a=float(input("Enter a: "))
    b=float(input("Enter b: "))
    c=float(input("Enter c: "))
    if(a>b and a>c):
        max=a
    elif(b>a and b>c):
        max=b
    else:
        max=c
    print(max)
except ValueError:
    print("Enter int or float values only")

