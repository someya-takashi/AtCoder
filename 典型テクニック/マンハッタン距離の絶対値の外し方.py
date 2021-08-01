# https://atcoder.jp/contests/abc210/tasks/abc210_d
# コスト = Aij + Ai'j' + C*(|i-i'|+|j+j'|)
# (i,j) != (i', j')で
# a'
#   a
# のように i >= i' かつ j >= j' のパターンと
#   a'
# a
# のように i >= i' かつ j <= j' のパターンを考える
# 前者は絶対値を普通に外す
# 後者はグリッドを左右反転させると前者のパターンに一致するので、同じ遷移プログラミングを使いまわせる

# 2次元累積minを更新しながら最小値を求めていく

H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

M = [[10**15] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        M[i][j] = A[i][j] - C*(i+j)
  
ans = 10**15

# パターン1の後にグリッドを左右反転させて2回評価を行う
for k in range(2):
    for i in range(H):
        for j in range(W):
            temp1 = 10**15
            temp2 = 10**15
            if i > 0:
                # 自身より上、自身と同じ位置から左の(i,j)までのグリッドのmin
                temp1 = M[i-1][j]
            if j > 0:
                # 自身と同じ位置から上、自身より左の(i,j)までのグリッドのmin
                temp2 = M[i][j-1]
            m = min(temp1, temp2)
            ans = min(ans, A[i][j] + C*(i+j) + m)
            if i > 0 or j > 0:
                # 自身と同じ(i,j)までの最小値を更新
                M[i][j] = min(M[i][j], m)
    
    # グリッドを左右反転し、再構築
    A = [A[i][::-1] for i in range(H)]
    for i in range(H):
        for j in range(W):
            M[i][j] = A[i][j] - C*(i+j)

print(ans)