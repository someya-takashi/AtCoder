# 区間DP（メモ化再帰）
# 区間DPは制約がO(N**2)かO(N**3)になることが多い
# 典型90 :019 https://atcoder.jp/contests/typical90/tasks/typical90_s
# Aからiとi+1を取り除くとき（コスト = |A[i]-A[i+1]|）、合計コストの最小値を求める
# dfs(0, 2N-1)から開始し、コストが確定するdfs(i, i+1)から漸化的にdpの値を更新していく
# 今回は初見だったのでわかりやすく[l, r]の開区間で実装
# 文献では[l, r) の半開半閉区間でやっている例が多いので、どちらで実装するか注意が必要

import sys
sys.setrecursionlimit(100000000)

N = int(input())
A = list(map(int, input().split()))
INF = 10**10

# 区間[l][r]に対応するdpテーブル
# dp[r][l]：lからrまでを削除する場合に必要なコストの最小値
dp = [[INF] * (2*N) for _ in range(2*N)]

def dfs(i, j):
    if dp[i][j] != INF:
        return dp[i][j]
    # Aにiとi+1しか残っていない場合
    # 再帰の最深層に対応
    if abs(i-j) == 1:
        dp[i][j] = abs(A[i]-A[j])
        return dp[i][j]
    
    # case1 : iとjを最後に除く場合
    res = abs(A[i]-A[j]) + dfs(i+1, j-1)

    # case2 : iからk-1, kからjまで除いた場合をすべて試し、番コストが小さい結果を保存
    for k in range(i+2, j, 2):
        res = min(res, dfs(i, k-1) + dfs(k, j))

    dp[i][j] = res
    return res

print(dfs(0, 2*N-1))