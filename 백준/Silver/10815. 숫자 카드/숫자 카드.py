
n=input()
hashTable=set(input().split())
m=input()
print(' '.join(['1' if num in hashTable else '0' for num in input().split()]))