"""
문제 유형 : 구현
예상 시간 : 30분
"""
def solution(genres, plays):
    answer = []
    dic = {i: {'total': 0, 'musics': []} for i in set(genres)}
    for i, (g, p) in enumerate(zip(genres, plays)):
        dic[g]['total']+=p
        dic[g]['musics'].append((i, p))
    for ID, genre in sorted([(item['total'], g) for g, item in dic.items()], key = lambda x: -x[0]):
        print(genre)
        sortedMusic = sorted(dic[genre]['musics'], key = lambda x: -x[1])[:2]
        answer += [i for i, p in sortedMusic]
    return answer