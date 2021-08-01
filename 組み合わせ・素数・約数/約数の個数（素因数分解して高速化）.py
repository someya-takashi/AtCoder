# 前計算：O(AloglogA)
# クエリ1回当たり：O(logA)

# Nを素因数分解したとき、要素の肩の値+1を掛け合わせると約数の個数になる
# 例：24 = 2**3 * 3**1 -> (3+1) * (1+1) = 8個


# 前計算
# 今回素因数分解する最大の数
MA = 10**7+10
sieve = [i for i in range(MA+1)]
p = 2
while p*p <= MA:
    if sieve[p] == p:
        for q in range(2*p,MA+1,p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1

# 前計算の結果を使って素因数分解を高速化
def f(n):
    ret = []
    while n > 1:
        ret.append(sieve[n])
        n //= sieve[n]
    return ret

N = int(input())
from collections import defaultdict
d = defaultdict(int)

# 素因数のカウント
prime = f(N)
for p in prime:
    d[p] += 1

# 約数の個数の計算
ans = 1
for v in d.values():
    ans *= (v+1)

print(ans)