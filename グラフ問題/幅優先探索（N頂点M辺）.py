# N頂点M本辺
N, M = map(int, input().split())
mod = 10**9+7
graph = [[] for _ in range(N)]

# 有向辺の場合は修正して使う
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# BFS部分
from collections import deque
Q = deque()
Q.append(0)
dist = [10**18] * N
dist[0] = 0

while Q:
    now = Q.popleft()

    for nxt in graph[now]:
        if dist[now] +1 < dist[nxt]:
            dist[nxt] = dist[now] + 1
            Q.append(nxt)

print(dist)