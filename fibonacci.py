num=int(input("enter a number:"))
a=0
b=1
if num<=0:
    print("enter a positive number")
elif num==1:
    print(f"the fibonacci of {num} is {a}")
else:
    print(a,b, end=" ")
    for i in range(2,num):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

