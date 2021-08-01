N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])

dist = [10**18] * N

import heapq
Q = []
# 頂点1からスタートする場合
heapq.heappush(Q, (0, 0))

while Q:
    d, i = heapq.heappop(Q)

    if d > dist[i]:
        continue

    for nxt, t in graph[i]:
        if d + t < dist[nxt]:
            dist[nxt] = d + t
            heapq.heappush(Q, (d + t, nxt))

print(dist)