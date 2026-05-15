text="hello"
rev=""
for i in text:
    result=i+rev
    rev=result
if rev==text:
    print("Palindrome")
else:
    print("Not a Palindrome")