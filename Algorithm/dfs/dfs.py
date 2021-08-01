import sys
sys.setrecursionlimit(1000000)

# 頂点数N, 辺情報E, 始点sとする

# N個のFalseで初期化した配列を用意
visited = []
for i in range(N):
    visited.append(False)

def dfs(i):
    visited[i] = True
    for j in E[i]:
        if not visited[j]:
            dfs(j)

dfs(s)