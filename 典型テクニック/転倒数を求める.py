# 1. 先頭から走査していく
# 2. 自身(A[i])のindexを+1する
# 3. これまでに出てきたi以上の数字をsum(i+1, N)で求め、転倒数に加算する

# Nlog(max(A))で転倒数を求められる

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

N = int(input())
A = list(map(int, input().split()))
MA = max(A)

bit = Fenwick_Tree(MA+1)
inv = 0
for i in range(N):
    bit.add(A[i], 1)
    # 自身より大きい数がi番目までに何個出てきたかを加算
    inv += bit.sum(A[i]+1, MA+1)

print(inv)