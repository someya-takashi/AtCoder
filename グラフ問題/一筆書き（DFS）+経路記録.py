# ヘビの場所が#で与えられるので、考えられるヘビの巻き方（一筆書き）を答える問題
# PAST : https://atcoder.jp/contests/past202012-open/tasks/past202012_g

import sys
sys.setrecursionlimit(100000000)

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# ヘビの長さを計算
snake = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            snake += 1

# すでに訪れたか
visited = [[False] * W for _ in range(H)]

from collections import deque
# 経路をdepueに保存
path = deque()

def dfs(i, j):
    # 訪れたのが二回目（これ以上伸ばせない）
    if visited[i][j]:
        count = 0
        for i2 in range(H):
            for j2 in range(W):
                if visited[i2][j2]:
                    count += 1
        # 訪れた回数がヘビの長さと同じなら、ヘビの頭から尾までの場所を出力して終了
        if count == snake:
            print(snake)
            for p1, p2 in path:
                print(p1, p2)
            exit()
        # 異なるなら適当に何か返して終了
        else:
            return False
    
    visited[i][j] = True
    # 行きがけに経路を追加
    path.append([i+1, j+1])

    # ..###..のように同じ場所に戻らない場合もあるので、visitedがTrueの場合と同じ処理を行う
    count = 0
    for i2 in range(H):
        for j2 in range(W):
            if visited[i2][j2]:
                count += 1
    if count == snake:
        print(snake)
        for p1, p2 in path:
            print(p1, p2)
        exit()

    # 隣接するマスに移動
    for k, l in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if 0 <= k < H and 0 <= l < W and grid[k][l] == "#":
            dfs(k, l)

    # ここに来るということは再帰先で答えのパスが見つからなかったということ
    # いまの経路は諦めるので、抜け駆けにvisitedをFalseにし、queからパスを削除する
    visited[i][j] = False
    path.pop()
    return False 

# すべての#が始点の候補なので、全探索する
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            dfs(i, j)