from collections import Counter
string = input()
counter = Counter(string)
c = sum(c%2 for c in counter.values())
if (len(string)%2 and c!=1) or (len(string)%2==0 and c!=0):
    print("I'm Sorry Hansoo")
else:
    answer, centerChar = '', ''
    if len(string):
        for key, val in counter.items():
            if val%2:
                centerChar = key
                counter[centerChar]-=1
                break
    for key in counter.keys():
        counter[key]//=2
    for key in sorted(counter.keys()):
        answer += key*counter[key]
    answer = answer+centerChar+answer[::-1]
    print(answer)