# 計算量 O((N+M)logM)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

# グラフに辺とコストを追加
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])

import heapq

marked = [False] * N

# マークした頂点数
marked_count = 0

# 適当な頂点からスタート
marked[0] = True
marked_count+=1

Q = []

# 始点の辺をヒープに追加
for i, c in graph[0]:
    heapq.heappush(Q, [c, i])

# 選んだ辺の総コスト
sum = 0

# すべての頂点をマークするまで
while marked_count < N:
    c, i = heapq.heappop(Q)

    if marked[i]:
        continue

    marked[i] = True
    marked_count+=1

    sum += c

    for j, c in graph[i]:
        if marked[j]:
            continue
        heapq.heappush(Q, [c, j])

print(sum) 