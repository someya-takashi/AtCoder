"""""
Replace Digits : https://atcoder.jp/contests/abl/tasks/abl_e

各桁の値を更新しながら、数値の余りを求める問題
桁数が10**5あるので、各桁毎にpow(10, i, mod)*xを計算し、その合計を答える必要がある

【改良点】
・i桁目のmodを高速に計算できるよう、self.mod[i] = pow(10, i, mod)を追加した

・区間更新のquery関数内で
    self.data[l] = (self.mod[l] * x)%mod
　のようにすぐに計算できるよう書き換えた（例：self.mod[4] = 1000）

・遅延評価の配列self.lazyには更新クエリの値dを保存しておき、遅延評価関数propagatesが呼ばれたときに
    self.lazy[2 * i] = v
    self.lazy[2 * i + 1] = v
    self.data[2 * i] = (self.mod[2*i]*v)%mod
    self.data[2 * i + 1] = (self.mod[2*i+1]*v)%mod
　のように書き換えた

・segfuncはreturn (x + y)%modにした
"""""

import sys
input = sys.stdin.readline
mod = 998244353

#####segfunc#####
def segfunc(x, y):
    return (x + y)%mod
#################

#####ide_ele#####
ide_ele = 0
#################

class LazySegmentTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(l, r, x): 区間[l, r)をxに更新 O(logN)
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
        # 修正点
        self.mod = [1] * 2 * self.num
        self.lazy = [None] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.data[self.num + i] = pow(10, n-i-1, mod) * init_val[i]
            self.mod[self.num + i] = pow(10, n-i-1, mod)
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])
            self.data[i] %= mod
            self.mod[i] = self.segfunc(self.mod[2 * i], self.mod[2 * i + 1])
            self.mod[i] %= mod

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
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            # 修正点
            self.data[2 * i] = (self.mod[2*i]*v)%mod
            self.data[2 * i + 1] = (self.mod[2*i+1]*v)%mod
            self.lazy[i] = None

    def update(self, l, r, x):
        """
        区間[l, r)の値をxに更新
        l, r: index(0-index)
        x: update value
        """
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                # 修正点
                self.data[l] = (self.mod[l] * x)%mod
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                # 修正点
                self.data[r - 1] = (self.mod[r-1] * x)%mod
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])
            self.data[i] %= mod

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
        return res%mod

N, Q = map(int, input().split())
A = [1] * N
sg = LazySegmentTree(A, segfunc, ide_ele)

for _ in range(Q):
    l, r, d = map(int, input().split())
    sg.update(l-1, r, d)
    ans = sg.query(0, N)
    print(ans%mod)
