from array import array
import bisect
# 第一引数は型を指定
A = array("i", [0, 10])

# インデックス1に5を挿入
A.insert(1, 5)

# 二分探索
idx = bisect.bisect_left(A, 6)


# 応用例：Cutting woods
# https://atcoder.jp/contests/abc217/tasks/abc217_d

from array import array
import bisect

L, Q = map(int, input().split())
A = array("i", [0, L])
ans = []
for _ in range(Q):
    c, x = map(int, input().split())
    idx = bisect.bisect_left(A, x)
    if c == 1:
        A.insert(idx, x)
    else:
        ans.append(A[idx]-A[idx-1])

print(*ans, sep="\n")