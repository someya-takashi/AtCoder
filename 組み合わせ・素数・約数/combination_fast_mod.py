#https://linus-mk.hatenablog.com/entry/2020/02/23/225258
#　フェルマーの小定理を用いたcombination計算の高速化
# n = 10**9, k = 10**5でも間に合う
# 階乗テーブルを作っていないのでNが大きいときにも都度計算可能
# 一回当たりの計算量がO(k)なので、Σkが大きくなると時間がかかる

n = int(input())

k = int(input())
mod = 10**9 + 7

#計算したいkについて階乗の逆元を前処理をしておく
modinv_table = [-1] * (k+1)
modinv_table[1] = 1
for i in range(2, k+1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans

print(binomial_coefficients(n, k))