# https://atcoder.jp/contests/abc103/tasks/abc103_d

N, M = map(int, input().split())

bridge = []
for _ in range(M):
    a, b = map(int, input().split())
    bridge.append([b, a])

# 区間の終端でソート
bridge.sort()

ans = 1
# 一番小さい終端からスタート
r = bridge[0][0]

for i in range(1, M):
    # 一番小さい終端を超える始点があった場合、串刺しできないので、答えを+1して新しい終点に更新する
    #    ----　　　　一番小さい終点
    #      -----
    #    --------
    #          ---   ここで更新
    #   -------------
    #             ------   ここで更新
    # 答え：3本
    if r <= bridge[i][1]:
        ans += 1
        r = bridge[i][0]

print(ans)