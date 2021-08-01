import sys
sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))
S = []
for i in range(H):
    s = input()
    S.append(s)

for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            si, sj = i, j
        if S[i][j] == "g":
            gi, gj = i, j
        
visited = []
for i in range(H):
    visited.append([False]*W)

def dfs(i, j):
    visited[i][j] = True
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
        if S[i][j] == "#":
            continue
        if not visited[i2][j2]:
            dfs(i2, j2)

dfs(si, sj)

if visited[gi][gj]:
    print("Yes")
else:
    print("No")