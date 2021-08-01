# https://atcoder.jp/contests/abc075/tasks/abc075_c

class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.par = [i for i in range(n)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * n

    def find (self, x):
        # 根ならその番号を返す
        if self.par[x] == x:
            return x
        # 根でないなら。親の要素で再検索
        else:
            # 走査していく過程で親を書き換える
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        # 木の高さを比較し、低いほうから高いほうに辺を張る
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
        # 木の高さが同じなら片方を1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

                
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
ans = 0

# 辺を一つずつ取り除き、非連結になるか確認
for removed_edge in edges:
    uf = UnionFind(N)

    # removed_edge以外の辺を張る
    for edge in edges:
        if edge == removed_edge:
            continue
        a, b = edge
        uf.union(a-1, b-1)

    # 経路圧縮しないと親の情報が更新されない
    for i in range(N):
        uf.find(i)

    # 親が一種類なら連結、一種類以上なら非連結
    if len(set(uf.par)) > 1:
        ans+=1

print(ans)