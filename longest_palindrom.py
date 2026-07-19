a=input("Enter the string:")
rev=""
for i in range (len(a)):
    for j in range(i+1,len(a)+1):
        sub=a[i:j]
        if sub==sub[::-1] and len(sub)>len(rev):
            rev=sub
print(rev)

