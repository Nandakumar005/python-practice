arr={10,30,30,20,20,10,40,50,-10,-50}
arr=list(arr)
print("Array:", arr)
largest=float('-inf')
second_largest=float('-inf')
for i in arr:
    if i>largest:
        largest=i   
    if i>second_largest and i!=largest:
        second_largest=i
print("Second Largest:", second_largest)
print("Largest:", largest)
