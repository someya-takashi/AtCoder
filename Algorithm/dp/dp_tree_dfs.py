import sys
sys.setrecursionlimit(1000000)

N = int(input())

# 親と子供の木構造、child[i] : i番目の親が持つ子の番号リスト
child = []
for i in range(N):
    child.append([])
for i in range(1, N):
    b = int(input())
    child[b-1].append(i)

# dfsで問題を解くロジックを実装
def dfs(i):
    if len(child[i]) == 0:
        return 1
    else:
        values = []
        for j in child[i]:
            values.append(dfs(j))
        return max(values) + min(values) + 1

print(dfs(0))