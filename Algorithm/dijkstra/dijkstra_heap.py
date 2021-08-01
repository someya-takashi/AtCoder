import heapq

N, M = map(int, input().split())

G = [[] for _ in range(N)]

cost = []
for i in range(N):
    cost.append([10**10]*N)

for _ in range(M):
    u, v, c = map(int, input().split())

    G[u].append(v)
    cost[u][v] = c

Q = []
heapq.heappush(Q, (0,0))

dist = [-1 for _ in range(N)]
dist[0] = 0

done = [False for _ in range(N)]

while len(Q) > 0:
    # d:距離、i:頂点
    d, i = heapq.heappop(Q)

    if done[i]:
        continue

    done[i] = True

    # Gは頂点と辺の親子関係を木構造で表す配列
    for j in G[i]:
        # 重み
        c = cost[i][j]

        #まだ見ていないか最短距離が更新できる場合
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))

print(dist[N-1])