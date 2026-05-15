ls=list([5, 2, 8, 1, 9,-8, 9, 7,0,80])
length=len(ls)
for i in range (length):
    for j in range(length):
        if ls[i] < ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print("Sorted Array:", ls)