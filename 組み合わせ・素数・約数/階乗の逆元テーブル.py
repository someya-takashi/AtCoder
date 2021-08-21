N = int(input())
mod = 10**9+7

fct = [1] * (N+2)
inv = [1] * (N+2)
for i in range(2, N+1): fct[i] = fct[i-1] * i % mod
inv[N] = pow(fct[N], mod-2, mod)
for i in range(N, 0, -1): inv[i-1] = inv[i] * i % mod