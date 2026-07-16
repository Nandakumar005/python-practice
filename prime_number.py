a=int(input("Enter a number:"))
if a<=0:
    print("Not a prime Number")
else:
    prime=True
    for i in range(2,int(a**5)+1):
        if a%i==0:
            prime=False
            break
if prime:
    print(f"{a} is a  prime number")
else:
    print(f"{a} is a not prime number")
    
