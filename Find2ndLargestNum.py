n = int(input("Enter how many numbers: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()

print("Second Largest Number =", numbers[-2])