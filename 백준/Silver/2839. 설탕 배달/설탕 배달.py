def sol(num):
    if num in (4, 7): return -1
    dic = {3: 3, 6: 6, 9: 9, 
           2: 12, 5: 0, 8: 18,
           1: 21, 4: 24, 7: 27, 0: 0}
    last1, last2 = num%10, (num-5)%10
    m = min(dic[last1], dic[last2])
    return (num-m)//5+m//3

print(sol(int(input())))