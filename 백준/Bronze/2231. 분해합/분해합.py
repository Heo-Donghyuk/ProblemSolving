target = int(input())
for num in range(1, target+1):
    temp = num+sum(int(i) for i in str(num))
    if temp==target:
        break
print(num if num!=target else 0)