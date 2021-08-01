import sys
sys.setrecursionlimit(100000000)

B = [list(map(int, input().split())) for _ in range(2)]
C = [list(map(int, input().split())) for _ in range(3)]

def points(g):
    chokudai = 0
    for i in range(2):
        for j in range(3):
            if g[i][j] == g[i+1][j]:
                chokudai += B[i][j]
    
    for i in range(3):
        for j in range(2):
            if g[i][j] == g[i][j+1]:
                chokudai += C[i][j]

    return chokudai

def dfs(turn):
    if turn == 10:
        return points(grid)
    
    if turn % 2 == 1:
        ret = -10**10
        for i in range(3):
            for j in range(3):
                if grid[i][j] == "":
                    grid[i][j] = "o"
                    ret = max(ret, dfs(turn+1))
                    grid[i][j] = ""
        
        return ret
    
    else:
        ret = 10**10
        for i in range(3):
            for j in range(3):
                if grid[i][j] == "":
                    grid[i][j] = "x"
                    ret = min(ret, dfs(turn+1))
                    grid[i][j] = ""
        
        return ret

grid = [[""] * 3 for _ in range(3)]

ans = dfs(1)

s = 0
for i in range(2):
    for j in range(3):
        s += B[i][j]
for i in range(3):
    for j in range(2):
        s += C[i][j]

print(ans)
print(s-ans)