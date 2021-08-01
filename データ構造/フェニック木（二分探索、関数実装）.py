# https://tjkendev.github.io/procon-library/python/range_query/bit.html
# A0 - AN-1の配列を管理する場合、以下のように初期化
#for i in range(N):
#    add(i, A[i])

# N: クエリ処理する列のサイズ
N = int(input())

data = [0]*(N+1)
# Akにxを追加
def add(k, x):
    while k <= N:
        data[k] += x
        k += k & -k

# A0 ~ Ak（kを含む）までの和を取得
def sum(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

# 二分探索
N0 = 2**(N-1).bit_length()
# O(logN)
# A0 + A1 + ... Ak <= xとなるインデックスkを取得
def lower_bound(x):
    w = i = 0
    k = N0
    while k:
        if i+k <= N and w + data[i+k] <= x:
            w += data[i+k]
            i += k
        k >>= 1
    return i+1