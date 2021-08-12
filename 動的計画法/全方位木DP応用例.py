# https://atcoder.jp/contests/dp/tasks/dp_v
# 参考：https://qiita.com/Kiri8128/items/a011c90d25911bdb3ed3

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

from collections import deque

# トポロジカルソート
P = [-1] * N
Q = deque([0])
R = []
while Q:
    i = Q.popleft()
    R.append(i)
    for n in graph[i]:
        if n != P[i]:
            P[n] = i
            graph[n].remove(i)
            Q.append(n)

##### Settings
unit = 1
def merge(a, b):
    return a * b % M
# ボトムアップの調整
def adj_bu(a, i):
    return a + 1
# トップダウンの調整
def adj_td(a, i, p):
    return a + 1
# 最終調整
def adj_fin(a, i):
    return a
#####

# ボトムアップ部分
ME = [unit] * N
dp = [0] * N
for i in R[1:][::-1]:
    dp[i] = adj_bu(ME[i], i)
    p = P[i]
    ME[p] = merge(ME[p], dp[i])
dp[R[0]] = adj_fin(ME[R[0]], R[0])

# トップダウン部分
TD = [unit] * N
for i in R:
    ac = TD[i]
    # 左からDP（結果はTDに入れている）
    for j in graph[i]:
        TD[j] = ac
        ac = merge(ac, dp[j])
    ac = unit
    # 右からDP（結果はacに入れている）
    for j in graph[i][::-1]:
        TD[j] = adj_td(merge(TD[j], ac), j, i)
        ac = merge(ac, dp[j])
        dp[j] = adj_fin(merge(ME[j], TD[j]), j)

for i in range(N):
    print(dp[i])