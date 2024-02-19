from collections import deque
n, k = map(int, input().split())
nums = [int(i) for i in input().split()]
answer = sorted(nums)
queue = deque([(nums, 0)])
visited = set(tuple(nums))
def BFS():
    while queue:
        arr, count = queue.popleft()
        if arr==answer:
            queue.clear()
            return count
        for i in range(n-k+1):
            element = (arr[:i]+arr[i:i+k][::-1]+arr[i+k:], count+1)
            key = tuple(element[0])
            if key not in visited:
                visited.add(key)
                queue.append(element)
    return -1

print(BFS())