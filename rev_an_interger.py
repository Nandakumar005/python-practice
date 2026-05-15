a=12345
result=0
while a!=0:
    digit=a%10
    result=result*10+digit
    a//=10
print(result)