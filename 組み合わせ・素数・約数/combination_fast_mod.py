#https://linus-mk.hatenablog.com/entry/2020/02/23/225258
#　フェルマーの小定理を用いたcombination計算の高速化
# n = 10**9, k = 10**5でも間に合う
# mod 素数 と組み合わせて使う（フェルマーの小定理を用いているため）


n = int(input())

k = int(input())
mod = 10**9 + 7

#計算したいkについてbinomial_coefficients関数を呼び出す前に前処理？をしておく
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