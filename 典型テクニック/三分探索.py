# ムーアの法則
# https://atcoder.jp/contests/arc054/tasks/arc054_b
# https://juppy.hatenablog.com/entry/2019/04/11/ARC054_-B_%E3%83%A0%E3%83%BC%E3%82%A2%E3%81%AE%E6%B3%95%E5%89%87_-_%E4%B8%89%E5%88%86%E6%8E%A2%E7%B4%A2_Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder

P = float(input())

# x年後に計算を始めた場合、x年とムーアの法則で計算量が2**(x/1.5)倍になったPの値を返す
def p(x):
    return x + P/(pow(2, x/1.5))

l = 0
r = 100 # 最大入力でも答えが90程度なので、それより大きい値で初期化


# while roopの部分は誤差を小さくしずぎると終わらないことがある
# 場合によってはfor i in range(10**5)など、規定回数で探索を終わらせることも考える
# p(x)が大きなる場合はwhile abs(r-l) > 10**(-7)の方が良さそう？
while abs(p(l)-p(r)) > 10**(-7):
    # lとrを三分割した領域で探索
    lp = p((2*l+r)/3)
    rp = p((l+2*r)/3)

    if lp > rp:
        l = (2*l+r)/3
    else:
        r = (l+2*r)/3

print(p((l+r)/2))