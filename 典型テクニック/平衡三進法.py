# 平衡三進法
# 通常の三進法では0, 1, 2の3つで表現するところを、-1, 0, 1の3つで表現する記法
# https://atcoder.jp/contests/past202107-open/tasks/past202107_g
# やり方：https://drken1215.hatenablog.com/entry/2019/10/18/135600
# Nを3で割りながら余りを見る
# 3で割った余りが1ならプラスの3のべき乗、2ならマイナスの3のべき乗を追加する

N = int(input())

ans = []
# べき乗の値：ループするごとに3倍していく
now = 1

while N > 0:
    if N % 3 == 1:
        ans.append(now)
        N -= 1
    elif N % 3 == 2:
        ans.append(-now)
        N += 1
    
    N //= 3
    now *= 3

print(len(ans))
print(" ".join(map(str, ans)))