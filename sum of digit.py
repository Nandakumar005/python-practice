num = int(input("Enter a number: "))
result = 0

if num <= 0:
    print("Enter a positive number")
else:
    num2 = [int(digit) for digit in str(num)]
    for i in num2:
        result = result + i
    print(f"Sum of digits: {result}")

