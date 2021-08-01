#https://atcoder.jp/contests/abc170/tasks/abc170_d
# エラトステネスの篩の応用
# Aを小さい順にソートし、Aの要素における素数を求めるようなイメージ
# 例：A=4, 8, 12, 24 では4がAの中で素数のように振る舞う

N = int(input())
A = list(map(int, input().split()))
A.sort()

A_max = A[-1]

# 0からA_maxまでの数のリスト
hurui = [True] * (A_max + 1)
ans = 0

for i in range(N-1):
    if hurui[A[i]]:
        # maxまでのA[i]の倍数を走査
        for j in range(A_max//A[i] + 1):
            hurui[A[i] * j] = False
        if A[i] != A[i+1]:
            ans += 1
if hurui[A_max]:
    ans += 1

print(ans)