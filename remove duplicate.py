n=int(input("enter the array size:"))
arr=[]
result=[]
for i in range (n):
     values=int(input("enter the values:"))
     arr.append(values)
for j in arr:
    if j not in  result:
        result.append(j)
arr=result
print(arr)

    
