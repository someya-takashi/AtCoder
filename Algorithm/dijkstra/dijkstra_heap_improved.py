import heapq

# 同じ頂点から重複して探索しないように改良したダイクストラ法
# 距離が最短の頂点が取り出されたとき、その頂点に対応するフラグを立てる

# 頂点のフラグ
done = [False for _ in range(N)]

while len(Q) > 0:
    # d:距離、i:頂点
    d, i = heapq.heappop(Q)

    if done[i]:
        continue

    done[i] = True

    # Gは頂点と辺の親子関係を木構造で表す配列
    for j in G[i]:
        # xは重み、今回は常に1とする
        x = 1

        if dist[j] == -1 or dist[j] > dist[i] + x:
            dist[j] = dist[i] + x
            heapq.heappush(Q, (dist[j], j))