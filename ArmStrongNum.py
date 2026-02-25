n = int(input("Enter number: "))

temp = n
count = len(str(n))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")