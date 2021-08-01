# 前計算を行い素因数分解を高速化
# 前計算をする分、1回当たりの素因数分解を高速化できるので、
# N = 10**6個の素因数分解をしても間に合い、クエリ処理等にも使える
# A = list(map(int, input().split()))
# MA = max(A)とすると
# 前計算　MAlog(logMA) + 素因数分解 logA[i]
# N個の素因数分解は　MAlog(logMA) + NlogMA


# 前計算
MA = 10**6+10
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