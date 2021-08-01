# N:数列の要素数, K:比較対象の整数
N, K = list(map(int, input().split()))
# 小さい順にソートされた数列
A = list(map(int, input().split()))

ok = N
ng = -1

while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if A[mid] >= K:
        ok = mid
    else:
        ng = mid

if ok == N:
    print(-1)
else:
    print(ok)