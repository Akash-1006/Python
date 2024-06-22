a=False
stack=[]
STR=input("Enter String: ")
for char in STR:
    if char == "(":
        stack.append(")")
    elif char == "[":
        stack.append("]")
    elif char == "{":
        stack.append("}")
    else:
        a=(stack.pop()==char)
if(a):
    print("Valid")
else:
    print("Invalid")
    
