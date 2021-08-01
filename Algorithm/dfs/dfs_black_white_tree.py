# uからvへの距離をN*Nの行列で保持したらTLEとMLEになってしまった
# 実装自体にエラーはなかったので、N*Nの行列の計算コストが高すぎた
# Nが大きいときはN*Nの行列を使うのは良くないかも（この問題ではN<=10**5）

import sys
sys.setrecursionlimit(10000000)

N = int(input())

tree = [[] for _ in range(N)]
color = [0] * N
visited = [False] * N

for _ in range(N-1):
    u, v, w = map(int, input().split())
    tree[u-1].append((v-1, w))
    tree[v-1].append((u-1, w))

def dfs(n):
    if visited[n]:
        return

    visited[n] = True

    for c, w in tree[n]:
        if w % 2 == 0:
            color[c] = color[n]
        else:
            color[c] = 1 - color[n]

        dfs(c)

dfs(0)

for i in range(N):
    print(color[i])