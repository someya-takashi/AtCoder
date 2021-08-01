# 船のコンテナのようにコンテナの上下の順序を保ったままコンテナを複数回移動し、場所を求める問題
# https://atcoder.jp/contests/past202005-open/tasks/past202005_k
# 単連結リストと関係があるらしい
# https://hamukichi.hatenablog.jp/entry/2020/06/07/160009

N, Q = map(int, input().split())

# コンテナiの真下にあるコンテナ
cont_bottom = [None] * N
# 机iのてっぺんにあるコンテナ
desk_top = [i for i in range(N)]

for _ in range(Q):
    f, t, x = map(int, input().split())
    f-=1
    t-=1
    x-=1

    # 後で更新前のdesk_top[f]を使うので、一時的に保存
    temp = desk_top[f]

    # f番目の机にあるx番目のコンテナを移動するので、新しいてっぺんコンテナはコンテナxの真下に
    # あるコンテナ = cont_bottom[x]になる
    desk_top[f] = cont_bottom[x]

    # コンテナxは机tに移動するので、コンテナxの真下のコンテナは机tのてっぺんにあるコンテナになる
    cont_bottom[x] = desk_top[t]

    # 机tのてっぺんコンテナは机fから移動してきたコンテナになる
    desk_top[t] = temp

# コンテナiが置かれている机の番号
cont_position = [None] * N

# 1~N番目の机についてtopから真下のコンテナがなくなるまで（cont_bottom[now] = None）コンテナを辿る
for i, cont in enumerate(desk_top):
    now = cont
    while now is not None:
        cont_position[now] = i
        now = cont_bottom[now]

for i in range(N):
    print(cont_position[i]+1)