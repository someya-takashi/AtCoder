H, W = map(int, input().split())

# 0度
T0 = [list(input()) for _ in range(H)]

# 90度回転
T1 = [[""] * H for _ in range(W)]
for i in range(W):
    for j in range(H):
        T1[i][j] = T0[j][W-i-1]

# 180度回転
T2 = [[""] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        T2[i][j] = T1[j][H-i-1]

# 270度回転
T3 = [[""] * H for _ in range(W)]
for i in range(W):
    for j in range(H):
        T3[i][j] = T2[j][W-i-1]