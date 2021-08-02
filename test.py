N = int(input())

mod = 10**9+7

class RepeatedPermutation():
  fct, inv = [], []
  mod = 10**9+7
  def __init__(self, imx, imod) -> None:
    self.mod = imod
    self.fct, self.inv = [1] * (imx+2), [1]* (imx+2)
    for i in range(2, imx+1): self.fct[i] = self.fct[i-1] * i % imod
    self.inv[imx] = pow(self.fct[imx], imod-2, imod)
    for i in range(imx, 0,-1): self.inv[i-1] = self.inv[i] * i % imod
  def pwr(self, n1, n2):
    return self.fct[n1+n2] * self.inv[n1] % self.mod  *self.inv[n2] % self.mod

p = RepeatedPermutation(N, mod)

ans = 0
ans += p.pwr(1,1)
ans += p.pwr(1,2)
ans += p.pwr(2,1)
ans += p.pwr(2,2)

print(ans)