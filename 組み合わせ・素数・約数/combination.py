from operator import mul
from functools import reduce

#どんなnに対しても速度が安定する方法
#nが大きいときに早い別の方法もある（https://qiita.com/derodero24/items/91b6468e66923a87f39f#%E3%83%A6%E3%83%BC%E3%82%B6%E5%AE%9A%E7%BE%A9%E5%9E%8B%EF%BC%92%E8%A9%95%E4%BE%A1-）
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

#ans = cmb(n, r)