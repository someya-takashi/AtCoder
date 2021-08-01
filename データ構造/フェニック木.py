# インスタンス化した後にaddで初期化する

class Fenwick_Tree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * n

    def add(self, p, x):
        # 0-indexed -> 1-indexed
        p += 1
        while p <= self.n:
            self.data[p-1] += x
            # 次に辿るindex
            # pに最下位bit（LSB）を加算
            p += p & -p

    # 1からrまでの総和
    # プライベート関数として実装
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r-1]
            # rから最下位bitを減算
            r -= r & -r
        return s

    # lからrまでの総和
    def sum(self, l, r):
        return self._sum(r) - self._sum(l)