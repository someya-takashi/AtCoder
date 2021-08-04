# 参考：https://drken1215.hatenablog.com/entry/2020/12/20/015100

# ax ≡ b (mod n) をxについて解く
# aの逆元が存在する→aとnが互いに素
# この場合は拡張ユーグリッドの互除法でaの逆元を求められる
# aとnが互いに素ではなくても、a,nに共通の約数が存在するなら、
# 最大公約数でそれぞれを割ることで、互いに素な方程式に帰着できる
# bがa, nの最大公約数で割り切れない場合は逆元が存在しない

# 1. とりあえずaとnのgcdを求める
# 2. bがgcdで割り切れるかを確認
# 3. gcdで割ったaとnから拡張ユーグリッドの互除法で逆元を求める

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

import math

a, b, n = map(int, input().split())

gcd = math.gcd(a, n)

if b % gcd != 0:
    print("逆元は存在しません")
    exit()

# gcdで割って互いに素な合同式に帰着させる
a //= gcd
b //= gcd
n //= gcd

# aのmod nでの逆元
ainv = modinv(a, n)

# x ≡ ainv*b (mod n)  
ans = (ainv*b)%n

print(ans)