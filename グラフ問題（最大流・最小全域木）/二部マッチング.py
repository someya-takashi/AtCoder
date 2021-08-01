# XとYの二部グラフの最大マッチング X={0,1,2,...|X|-1} Y={0,1,2,...,|Y|-1}
#   edges[x]: xとつながるYの頂点のset
#   matched[y]: yとマッチングされたXの頂点(暫定)
 
def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False
 
 
# 標準入力からのグラフ読み取り
# xn:グラフXの頂点数、yn:グラフYの頂点数、e:XとY間のエッジの数
xn, yn, e = map(int, input().split())
edges = [set() for _ in range(xn)]
matched = [-1] * yn

# エッジを追加
for _ in range(e):
    x, y = map(int, input().split())
    edges[x].add(y)
 
# 増大路発見に成功したらTrue(=1)。合計することでマッチング数となる
print(sum(dfs(s, set()) for s in range(xn)))