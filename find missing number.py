arr = [1,2,3,5,6,9]
missing = []
for i in range(len(arr) - 1):
    if arr[i] + 1 != arr[i + 1]:
        for num in range(arr[i] + 1, arr[i + 1]):
            missing.append(num)
print(missing)
   
