num=int(input("Enter a number:"))
fact=1
if num<=0:
    print("enter a positive number:")
elif num==1:
    print("The factorial of 1 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
print(f"The factorial of {num} is {fact}")