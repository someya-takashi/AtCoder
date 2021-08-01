H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]

ALL = 1<<(H-1)

lines = [[0] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "0":
            w = 1
        else:
            w = 0
        lines[i].append(lines[i][j]+w)

ans = 10**10
for i in range(ALL):
    cuth = [0]
    for j in range(H-1):
        if i & 1<<j:
            cuth.append(j)
    cutw  = []
    last = 0
    for k in range(W):
        for l in range(len(cuth)-1):
            up = cuth[l]
            down = cuth[l+1]
            w = 0
            for m in range(up, down):
                w += lines[m][k]
            
            if w > K:
                break


            





