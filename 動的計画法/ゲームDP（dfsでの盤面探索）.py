# ゲームDP
# 相手の手番に行き止まりなら勝ち
# 右、右下、下の遷移があるので、メモ化再帰ですべてのマスの勝敗を探索する
# 計算量はO(HW)
# 右、右下、下どこに移動しても相手が勝つようなセルは負けセル
# 右、右下、下どこか一か所でも相手が負けるようなセルは勝ちセル


H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

memo = [[None] * (W+1) for _ in range(H+1)] 

def dfs(i,j):
    if memo[i][j] != None:
        return memo[i][j]
    
    # iかjが番外か障害物
    if i + 1 > H or j + 1 > W or grid[i][j] == "#":
        memo[i][j] = True
        return True

    # 次のセルが負けセルなら、相手に負けセルを押し付けられるので、現在のセルは勝ちセル
    if not dfs(i+1, j):
        memo[i][j] = True
        return True
    if not dfs(i, j+1):
        memo[i][j] = True
        return True
    if not dfs(i+1, j+1):
        memo[i][j] = True
        return True
    
    # 移動候補が全て勝ちセルなら、相手が勝ちセルに移動してしまうので、現在のセルは負けセル
    memo[i][j] = False
    return False

if dfs(0,0):
    print("First")
else:
    print("Second")