import heapq

N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    # 始点、終点、コスト
    u, v, c = map(int, input().split())

    # 無向グラフなので両方向を追加
    G[u].append((v, c))
    G[v].append((u, c))

marked = [False for _ in range(N)]
marked_count = 0

marked[0] = True
marked_count+=1

Q = []

# 始点からの移動候補
for j, c in G[0]:
    heapq.heappush(Q, (c, j))

sum = 0

while marked_count < N:

    c, i = heapq.heappop(Q)

    if marked[i]:
        continue

    marked[i] = True
    marked_count += 1

    sum += c

    # 次の頂点候補をヒープに追加
    for (j, c) in G[i]:

        if marked[j]:
            continue
        heapq.heappush(Q, (c, j))

print(sum)