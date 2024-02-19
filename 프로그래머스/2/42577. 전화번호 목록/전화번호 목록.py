def solution(phone_book):
    dic = set()
    for num in sorted(phone_book, key=len):
        for i in range(1,len(num)+1):
            if num[:i] in dic:
                return False
        dic.add(num)
    return True