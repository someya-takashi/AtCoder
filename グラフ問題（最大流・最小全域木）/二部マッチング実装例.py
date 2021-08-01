# https://atcoder.jp/contests/abc091/tasks/arc092_a
# 二次元上の赤い点と青い点の組み合わせ可能な最大数を求める問題
# 貪欲法でも解けるが、二部マッチングを用いると考察と実装が楽

N = int(input())
R = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    R.append([a, b])

for i in range(N):
    c, d = map(int, input().split())
    B.append([c, d])

# 組み合わせ可能な赤と青
edges = [set() for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 組み合わせ可能なら辺を追加
        if R[i][0] < B[j][0] and R[i][1] < B[j][1]:
            edges[i].add(j)

# テンプレそのまま使用
def dfs(v, visited):
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False

# XとYの二部グラフがあるとしてYの方の頂点数の配列
matched = [-1] * N

print(sum(dfs(s, set()) for s in range(N)))