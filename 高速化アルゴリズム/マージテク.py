# 例題：Confluence　https://atcoder.jp/contests/abc183/tasks/abc183_f
# 集合同士をマージするとき、要素数の小さい集合を大きい集合にマージすることで、
# 各要素の移動回数をO(logN)に抑制する手法

# 今回はグループ番号毎に各クラスの人数を管理する class_manager (defaultdict(int)の配列)で
# i番目のグループのクラスjの人数をclass_manager[i][j]で持つ

# xとyのグループのマージの際はclass_manager[x]とclass_manager[y]をマージする


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]  # 親
        self.rank = [1] * n  # 木の高さ
        self.size = [1] * n  # size[i] は i を根とするグループのサイズ
 
    def find(self, x):  # x の根を返す
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
            return self.parent[x]
 
    def unite(self, x, y):  # x, y の属する集合を併合する
        x = self.find(x)
        y = self.find(y)
        if x != y:
            # 元々はランクでマージする側を決めていたが、今回はグループサイズで判定する
            if self.group_size(x) < self.group_size(y):
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
 
    def is_same(self, x, y):  # x, y が同じ集合に属するか判定する
        return self.find(x) == self.find(y)
 
    def group_size(self, x):  # x が属する集合の大きさを返す
        return self.size[self.find(x)]
 
    def group_members(self, x):  # x が属する集合の要素を返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):  # すべての根をリストで返す
        return [i for i, x in enumerate(self.parent) if i == x]
 
    def group_count(self):  # 木の数を返す
        return len(self.roots())
 
    def __str__(self):  # print 表示用
        return '\n'.join('{}: {}'.format(r, self.group_members(r)) for r in self.roots())


from collections import defaultdict
N, Q = map(int, input().split())
C = list(map(int, input().split()))

class_manager = [defaultdict(int) for _ in range(N)]
for i in range(N):
    class_manager[i][C[i]-1] += 1

uf = UnionFind(N)

for _ in range(Q):
    n, x, y = list(map(int, input().split()))
    x-=1
    y-=1
    if n == 1:
        # 要素数の大きい方をxとする
        if uf.group_size(y) > uf.group_size(x):
            x, y = y, x

        # 親の番号を取得し、親のclass_managerをマージする
        rx = uf.find(x)
        ry = uf.find(y)
        if rx == ry:
            continue

        # マージ基準をランクからグループサイズに書き換え（30行目）
        uf.unite(x, y)

        # class_managerをマージ
        # yのclass_managerを0にし、xに加算
        for c, v in class_manager[ry].items():
            class_manager[rx][c] += v
            class_manager[ry][c] = 0
        
    else:
        rx = uf.find(x)
        print(class_manager[rx][y])

