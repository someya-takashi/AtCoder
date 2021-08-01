# 重さの合計がXになる制約があるため、片方のグループの重さが
# もう片方のグループの重さからXを引いた分に一致するかを半分ずつ
# 調べることで、2**Nの計算量を2**(N/2)に削減できる

from collections import defaultdict

N, X = list(map(int, input().split()))

A = []
B = []
for i in range(N):
    w = int(input())
    if i%2 == 0:
        A.append(w)
    else:
        B.append(w)

def has_bit(n, i):
    return (n & (1<<i) > 0)

for n in range(2**len(B)):
    wb = 0
    for i in range(N):
        if has_bit(n, i):
            wb += B[i]
    dic[wb] += 1

ans = 0
for n in range(2**len(A)):
    wa = 0
    for i in range(N):
        if has_bit(n, i):
            wa += A[i]
    ans += dic[x-wa]

print(ans)