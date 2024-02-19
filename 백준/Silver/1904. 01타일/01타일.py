num1, num2 = 1, 1
for i in range(int(input())-1):
    num1, num2 = num2, (num1+num2)%15746
print(num2)