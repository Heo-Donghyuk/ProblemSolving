from collections import defaultdict, deque
import sys

input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

N, K, R = map(int, input().split())

cal_actual_coord = lambda x : int(x) - 1
road_count_dict = defaultdict(list)
node_count_dict = defaultdict(int)

def road_init() :
  for _ in range(R) :
    r1, c1, r2, c2 = map(cal_actual_coord, input().split())
    road_count_dict[(r1, c1)].append((r2, c2))
    road_count_dict[(r2, c2)].append((r1, c1))

def bfs(r, c, idx_cnt, visited) :
  q = deque([(r, c)])
  visited[r][c] = idx_cnt

  while q :
    r, c = q.popleft()

    for k in range(4) :
      ar, ac = r + dr[k], c + dc[k]
      if -1 < ar < N and -1 < ac < N and visited[ar][ac] == -1 and (ar, ac) not in road_count_dict[(r, c)] :
        visited[ar][ac] = idx_cnt
        q.append((ar, ac))

def full_search() :
  idx_cnt = 0
  visited = [[-1]*N for _ in range(N)]
  for i in range(N) :
    for j in range(N) :
      if visited[i][j] == -1 :
        bfs(i, j, idx_cnt, visited)
        idx_cnt += 1

  return visited, idx_cnt

def cow_init(visited) :
  for _ in range(K) :
    r, c = map(cal_actual_coord, input().split())
    lands = visited[r][c]
    node_count_dict[lands] += 1

def cal_result(idx_cnt) :
  result = 0
  for i in range(idx_cnt-1) :
    for j in range(i+1, idx_cnt) :
      result += node_count_dict[i] * node_count_dict[j]

  print(result)

def solve() :
  road_init()
  visited, idx_cnt = full_search()
  cow_init(visited)
  cal_result(idx_cnt)

solve()