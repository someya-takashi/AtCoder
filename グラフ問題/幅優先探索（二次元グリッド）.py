from collections import deque

H, W = map(int, input().split())
# "."と"#"のような文字列のグリッド
S = [list(input()) for _ in range(H)]
# コストなど数値情報の場合
# A = [list(map(int, input().split())) for _ in range(H)]

dist = [[10**18] * W for _ in range(H)]

Q = deque()
Q.append([0, 0])
dist[0][0] = 0

while len(Q) > 0:
    i, j = Q.popleft()

    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if 0 <= i2 < H and 0 <= j2 < W and S[i2][j2] == ".":
            if dist[i][j] + 1 < dist[i2][j2]:
                dist[i2][j2] = dist[i][j] + 1
                Q.append([i2, j2])

print(dist)