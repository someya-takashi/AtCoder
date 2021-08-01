# AtCoder ABC041D 徒競走
# DAGのトポロジカルソートの数え上げ問題
# bitDP
# 計算量 O(N*2**N)

# N : 頂点数, M : 有向辺の数
N, M = map(int, input().split())
# i -> j の有向辺が存在するかのN*N行列
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    # aからbへ有向辺を張る
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

ALL = 1 << N
dp = [0] * ALL
# 空集合のとき、トポロジカルソートの方法は一つ
dp[0] = 1

# 空集合からすべてのうさぎの集合までループし、DPを構築
for i in range(ALL):
    # 新たに状態iに追加する頂点候補jについてループ
    for j in range(N):
        # 集合iにすでにjが含まれているなら、パス
        if i & 1 << j:
            continue
        # まだ含まれていないなら、現在のトポロジカルソートiにjを追加できるかチェック
        # 上記を確認するフラグ
        flag = True
        # 追加できない条件：集合iに含まれている頂点kへjからkに伸びる有向辺が存在する
        # (k ∈ i)　<- j
        # このとき、トポロジカルソートの順序に問題があるため、このようなソートは存在しない
        for k in range(N):
            if i & 1 <<k and graph[j][k]:
                flag = False
                break
        
        # 上記のチェックでフラグが破られなかった場合は新たにjを
        # 追加してできるトポロジカルソート（i | 1 <<j）が存在する
        if flag:
            # トポロジカルソート（i | 1 <<j）へは様々なiからの遷移が
            # 考えられるので、遷移元の組み合わせを足していく
            dp[i | 1 << j] += dp[i]

# すべての部分的なトポロジカルソートiから全頂点集ALLへの遷移を足し上げたものが答え
print(dp[ALL-1])