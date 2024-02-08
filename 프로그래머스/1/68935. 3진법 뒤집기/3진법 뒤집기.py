def decToTri(num):
    k, res = 0, ''
    while 3**k<num:
        k+=1
    while k+1:
        res+=str(num//(3**k))
        num = num%(3**k)
        k-=1
    return int(res)
def triToDec(num):
    res = 0
    for k, n in enumerate(str(num)[::-1]):
        res+=int(n)*(3**k)
    return res
def solution(n):
    return triToDec(int(str(decToTri(n))[::-1]))