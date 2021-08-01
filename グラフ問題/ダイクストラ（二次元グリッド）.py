# 調整箇所はコメントの直後の行

H, W = map(int, input().split())

# 各マスのコストに応じて変更
A = [list(map(int, input().split())) for _ in range(H)]

dist = [[10**15] * W for _ in range(H)]

import heapq
Q = []

# スタート地点に応じて変更
heapq.heappush(Q, (0, 0, 0))
dist[0][0] = 0

while Q:
    cost, i, j = heapq.heappop(Q)

    if cost > dist[i][j]:
        continue

    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        # 障害物ある場合など、遷移不可の条件が必要なら追加
        if 0 <= i2 < H and 0 <= j2 < W:

            # コストの更新方法に応じて微調整
            next_cost = cost + A[i2][j2]

            if next_cost < dist[i2][j2]:
                dist[i2][j2] = next_cost
                heapq.heappush(Q, (next_cost, i2, j2))

print(dist)