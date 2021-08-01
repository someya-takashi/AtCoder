# 自作、競プロ典型30より
# O(Nlog(logN)) 10**7も可
N = int(input())

c = [True] * (N+1)
def f(N):
    for i in range(2, N+1):
        if c[i] != True:
            continue
        # 素数の倍数をFalseにしていく
        for j in range(i, N+1, i):
            if j == i:
                continue
            c[j] = False
    # c[i] = True つまり素数を返却
    return [i for i in range(2, N+1) if c[i]]

print(len(f(N)))


# https://inarizuuuushi.hatenablog.com/entry/2016/12/13/092024
# 10**5でも一瞬で列挙できる、おすすめ
# O(Nlog(logN))
from math import sqrt, ceil

def era_prime(N):
    temp = [True]*(N+1)
    temp[0] = temp[1] = False
    for i in range(2, ceil(sqrt(N+1))):
        if temp[i]:
            temp[i+i::i] = [False]*(len(temp[i+i::i]))                            
    primes = [ n for n in range(N+1) if temp[n] ]
    return primes



# 10000だと遅い、間に合わない
pn=[2];A=1000
for L in range(3,A):
    chk=True
    for L2 in pn:
        if L%L2 == 0:chk=False
    if chk:pn.append(L)
print(pn)





# https://qiita.com/st1711713/items/f5cbda3a93e3eeec147a
# 100000だとこっちのほうが早い
sosuu = [2]
A = 100000
for L in range(3, A, 2): # 2 以外の素数は奇数なので
    for L2 in sosuu:
        if L % L2 == 0:
            break # 素数でないことがわかったらそれ以上ループする必要はない
    else: # break で抜けることがなかったら L は素数（Python 特有の制御構文）
        sosuu.append(L)
print(sosuu)