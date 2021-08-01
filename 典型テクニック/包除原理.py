# 包除原理 https://atcoder.jp/contests/typical90/tasks/typical90_cb
# https://compro.tsutaj.com//archive/181015_incexc.pdf
# https://qiita.com/DaikiSuyama/items/4d0388a3f68b60c3e5f3
# https://satanic0258.hatenablog.com/entry/2016/04/10/104524

N, D = map(int, input().split())
A = list(map(int, input().split()))

# 余事象であるAi&x==0となる数を数え、2**Dから引くことを考える
# Ai&x=0となるxの集合をXiとする
# すべてのAiの部分集合について対応する部分集合Xiの要素数を計算し、包除原理でXi全体の和集合を求める
# 部分集合の要素数が奇数の時は加算、偶数の時は減算
# N = 2のときはベン図で簡単にわかる X1∪X2 = X1 + X2 - X1 ∩ X2
# 一般のNについては上記の偶奇で符号を判定する
# 例として、N = 3では　X1∪X2∪X3 = X1 + X2 +X3 - X1∩X2 - X2∩X3 - X1∩X3 + X1∩X2∩X3

ans = 0
ALL = 1 << N
# すべての積集合（空集合を除く）を調べる
for i in range(1, ALL):
    bit = 0
    n = 0
    # Ajのor演算を取り、後で0のbitを集計
    for j in range(N):
        if i & 1 << j:
            bit |= A[j]
            n += 1
    
    count = 0
    # 0にするにはbitが1のところは0の1通り、bitが0のところは0でも1でもいいので2通り可
    # 0になるxの総数は2**count通り
    for k in range(D):
        if bit & 1 << k == 0:
            count += 1

    if n % 2 == 0:
        ans -= 2 **count
    else:
        ans += 2 **count

# 全体からX1∪X2∪...∪XNを引く
print(2**D-ans)