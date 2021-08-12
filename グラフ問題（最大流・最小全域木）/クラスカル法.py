# 計算量 O(ElogV) or O(ElogE)
# 辺のソート：O(ElogE)
# 最小全域木の構築：O(ElogV)

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

    def unite(self, x, y):
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
edge = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append([a-1, b-1, c])

edge.sort(key=lambda x:x[2])

cost = 0
uf = UnionFind(N)

# 辺のコストを昇順に見てaとbが連結でないなら辺を追加
for a, b, c in edge:
    if not uf.same_check(a, b):
        uf.unite(a, b)
        cost += c

print(cost)