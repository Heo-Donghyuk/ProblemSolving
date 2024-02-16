import sys


def find_root(group, a):
    if group[a] == a:
        return a

    group[a] = find_root(group, group[a])
    return group[a]


def union(group, root_a, root_b):

    if root_a < root_b:
        group[root_b] = root_a
    else:
        group[root_a] = root_b


def solution(n, edge):

    group = list(range(n+1))
    edge.sort(key=lambda x: x[0])

    sum = 0
    max = 0
    count = 0
    n_1 = n - 1

    for cost, a, b in edge:

        root_a = find_root(group, a)
        root_b = find_root(group, b)

        if root_a == root_b:
            continue

        union(group, root_a, root_b)
        sum += cost
        max = cost
        count += 1

        if count == n_1:
            break

    return sum - max


def main():
    input = sys.stdin.readline
    n, e = map(int, input().split())

    edge = []
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edge.append((cost, a, b))

    print(solution(n, edge))


if __name__ == "__main__":
    main()