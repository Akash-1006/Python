def add(a, b):
    res=a+b
    return res

def sub(a,b):
    res= a-b
    return res

def mul(a,b):
    res= a*b
    return res


def div(a,b):
    res=a/b
    return res
   
a = float(input(" Enter value for a: "))
b = float(input(" Enter value for b: "))
print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division\n")
choice= int(input(" Enter your choice: "))

    
if choice == 1:
    print("Sum is ",add(a,b))
elif choice == 2:
    print("Difference is :", sub(a,b))
elif choice == 3:
    print("Product is ", mul(a,b))
elif choice == 4:
    print("Quotient is :", div(a,b))
else:
    print("Invalid input")


















    
