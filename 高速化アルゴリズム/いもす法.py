# imos法
# https://atcoder.jp/contests/abc035/tasks/abc035_d

N, Q = map(int, input().split())

othello = [0] * N
# オセロの裏返させた範囲と回数を記録し、最後にまとめて計算
for i in range(Q):
    l, r = map(int, input().split())
    # 始点を+1
    othello[l-1] += 1
    # 終点+1を-1、r = Nなら-1しない
    if r < N:
        othello[r] -= 1

# 累積和
for i in range(1, N):
    othello[i] += othello[i-1]

ans = [str(x % 2) for x in othello]
print("".join(ans))