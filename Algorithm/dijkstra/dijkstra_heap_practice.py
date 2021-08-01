# 深さ優先探索で解ける問題をヒープを用いて解いた場合
# 辺の重みは1

import heapq
N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(0, M):
    ai, bi = map(int, input().split())

    ai -= 1
    bi -= 1

    G[ai].append[(bi)
    G[bi].append(ai)

dist = [-1 for _ in range(N)]

Q = []

# (距離, 頂点)
heapq.heappush(Q, (0,0))

dist[0] = 0

while len(Q) > 0:
    d, i = heapq.heappop(Q)

    for j in G[i]:
        # 重みは常に1の場合
        x = 1

        if dist[j] == -1 or dist[j] > dist[i] + x:
            dist[j] = dist[i] + x
            heapq.heappush(Q, (dist[j], j))

if dist[N-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
