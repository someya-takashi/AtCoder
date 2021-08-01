# 区間最大＋区間加算（減算）
# Silver Fox vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_f

import sys
input = sys.stdin.readline

#####segfunc#####
def segfunc(x, y):
    return max(x, y)
#################

#####ide_ele#####
ide_ele = - (2**31 - 1)
#################

class LazySegmentTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    add(l, r, x): 区間[l, r)にxを加算 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        num: n以上の最小の2のべき乗
        data: 値配列(1-index)
        lazy: 遅延配列(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.data = [ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.data[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def gindex(self, l, r):
            """
            伝搬する対象の区間を求める
            lm: 伝搬する必要のある最大の左閉区間
            rm: 伝搬する必要のある最大の右開区間
            """
            l += self.num
            r += self.num
            lm = l >> (l & -l).bit_length()
            rm = r >> (r & -r).bit_length()

            while r > l:
                if l <= lm:
                    yield l
                if r <= rm:
                    yield r
                r >>= 1
                l >>= 1
            while l:
                yield l
                l >>= 1

    def propagates(self, *ids):
        """
        遅延伝搬処理
        ids: 伝搬する対象の区間 
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if not v:
                continue
            self.lazy[2 * i] += v
            self.lazy[2 * i + 1] += v
            self.data[2 * i] += v
            self.data[2 * i + 1] += v
            self.lazy[i] = 0

    def add(self, l, r, x):
        """
        区間[l, r)の値にxを加算
        l, r: index(0-index)
        x: additional value
        """
        *ids, = self.gindex(l, r)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] += x
                self.data[l] += x
                l += 1
            if r & 1:
                self.lazy[r - 1] += x
                self.data[r - 1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1]) + self.lazy[i]


    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res

N, D, A = map(int, input().split())
enemy = []
for _ in range(N):
    x, h = map(int, input().split())
    enemy.append([x, h])

enemy.sort(key=lambda x:x[0])
import bisect
ans = 0

H = [enemy[i][1] for i in range(N)]
X = [enemy[i][0] for i in range(N)]

sg = LazySegmentTree(H, segfunc, ide_ele)

ptr = 0
while sg.query(0, N) > 0:
    while sg.query(ptr,ptr+1) > 0:
        # 左端は生きているモンスターの中で一番左
        l = ptr
        # 爆発の範囲の右端を二分探索で求める
        r = bisect.bisect_right(X, X[ptr] + 2 * D)

        # 一番左のモンスターを倒すために必要な爆発回数
        num = -(-sg.query(ptr,ptr+1)//A)
        # ダメージを減算
        sg.add(l, r, -A*num)
        # 爆発回数をansに追加
        ans += num

    # まだ生きているモンスターまでポインターを進める
    while sg.query(ptr,ptr+1) <= 0:
        ptr+=1
        if ptr == N:
            break

print(ans)
