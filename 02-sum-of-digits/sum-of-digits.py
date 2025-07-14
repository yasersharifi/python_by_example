num1 = int(input("Enter the number: "))

sumOfDigits = 0
digitsCount = 0
remaining = -1

if (num1 <= 0):
    print("Enter the number bigger than 0")
    exit()

while True:
    remaining = num1 % 10
    digitsCount += 1
    sumOfDigits += remaining
    num1 = num1 // 10

    if num1 == 0:
        break

print(f"Digits count: {digitsCount}")
print(f"Sum of digits: {sumOfDigits}")

