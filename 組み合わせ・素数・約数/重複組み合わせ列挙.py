# https://atcoder.jp/contests/abc165/tasks/abc165_c
N, M, Q = map(int, input().split())

q = []
for _ in range(Q):
    l = list(map(int, input().split()))
    q.append(l)

# 重複組み合わせを列挙する関数
from itertools import combinations_with_replacement

# 例：combinations_with_replacement(range(1, 5), 3)
# 1~4のボールを袋から取り出し、また袋に戻して合計3回取り出す組み合わせ
# (1, 1, 1)
# (1, 1, 2)
# (1, 1, 3)
# (1, 1, 4)
# (1, 2, 2)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 3)
# (1, 3, 4)
# (1, 4, 4)
# (2, 2, 2)
# (2, 2, 3)
# (2, 2, 4)
# (2, 3, 3)
# (2, 3, 4)
# (2, 4, 4)
# (3, 3, 3)
# (3, 3, 4)
# (3, 4, 4)
# (4, 4, 4)

ans = 0
for p in combinations_with_replacement(range(1, M+1), N):
    point = 0
    for i in range(Q):
        a, b, c, d = q[i]
        if p[b-1] - p[a-1] == c:
            point+=d

    ans = max(ans, point)

print(ans)
