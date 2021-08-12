# 約数系包除原理
# 1からNまでの整数でgcd(x, y) = K となる(x, y)の組み合わせを求める
N = int(input())
K = int(input())

# 1-index
# F[g] = 1からN以下のx, yでgcd(x, y) = g となる(x, y)の組み合わせの数
F = [0] * (N+1)

# Nまでにgの倍数がいくつあるか（x, yそれぞれについて(N//g)通りなので二乗）
for g in range(1, N+1):
    F[g] = (N//g)**2

# gのk倍の重複を包除原理で取り除く
# 例えばg=2のとき(x, y) = (4, 8) = gcd = 4なども数え上げているので, F[2]からF[4], F[6]など倍数成分を減算
for g in range(1, N+1)[::-1]:
    fg = F[g]
    k = 2*g
    while k <= N:
        fg -= F[k]
        k += g
    
    F[g] = fg

print(F[K])