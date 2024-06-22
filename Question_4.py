n=1
amount=0
for i in range (0,4):
    print("Enter denomination ",n)
    den=int(input())
    print("Enter number of notes for denomination ",n)
    note=int(input())
    amount=amount+(den*note)
    n+=1
print("Total available balance in ATM is: ",amount)
