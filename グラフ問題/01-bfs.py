# https://atcoder.jp/contests/abc176/tasks/abc176_d
# コストがかからない通常移動はappendleft, コストがかかる魔法移動はappend

H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())

from collections import deque

# 魔法を使う場合の5*5の移動
dh = [-2, -1, 0, 1, 2]
dw = [-2, -1, 0, 1, 2]

maze = [input() for _ in range(H)]

# 0-indexed
Ch-=1
Cw-=1
Dh-=1
Dw-=1

Q = deque()
cost = [[10**10] * W for _ in range(H)]

Q.append((Ch, Cw))
cost[Ch][Cw] = 0

# 0-1bfs開始
while len(Q):
    h, w = Q.popleft()
    for i in range(5):
        for j in range(5):
            nh, nw = h+dh[i], w+dw[j]

            # これで通常移動と魔法移動の判別を行う
            dist = abs(dh[i]) + abs(dw[j])

            if nh < 0 or H <= nh or nw < 0 or W <= nw:
                continue
            if maze[nh][nw] == "#":
                continue

            # 通常移動でコストが更新できる場合
            # 左にプッシュ
            if dist <= 1:
                if cost[nh][nw] > cost[h][w]:
                    cost[nh][nw] = cost[h][w]
                    Q.appendleft((nh, nw))
            
            # 魔法移動でコストが更新できる場合
            # 右にプッシュ
            else:
                if cost[nh][nw] > cost[h][w] + 1:
                    cost[nh][nw] = cost[h][w] + 1
                    Q.append((nh, nw))
    
ans = cost[Dh][Dw]

if ans == 10**10:
    print(-1)
else:
    print(ans)