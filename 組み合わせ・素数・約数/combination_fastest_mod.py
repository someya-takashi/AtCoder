# https://atcoder.jp/contests/abc151/submissions/22708317
# N<10**5、K<10**5で最大N回の組み合わせ計算がある問題で使用した
# 逆元の前計算をしているのでO(1)

N = int(input())
K = int(input())
mod = 10**9+7

class Ncrs():
  fct, inv = [], []
  mod = 10**9+7
  def __init__(self, imx, imod) -> None:
    self.mod = imod
    # 階乗および階乗の逆元
    self.fct, self.inv = [1] * (imx+2), [1]* (imx+2)
    for i in range(2, imx+1): self.fct[i] = self.fct[i-1] * i % imod
    # フェルマーの小定理：a**(p-2) (mod p)がaの逆元
    self.inv[imx] = pow(self.fct[imx], imod-2, imod)
    for i in range(imx, 0,-1): self.inv[i-1] = self.inv[i] * i % imod
  def nck(self, n, k):
    if k > n or n <0 or k <0: return 0
    return self.fct[n] * self.inv[k] % self.mod  *self.inv[n-k] % self.mod

r = Ncrs(N, mod)

print(r.nck(N, K))
