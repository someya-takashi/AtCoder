mod = 10**9+7
s = 10**9+2
a = (s)%mod
b = (a*(s-1))%mod
c = (b*(s-2))%mod

d = pow(6, mod-2, mod)

print((c*d)%mod)