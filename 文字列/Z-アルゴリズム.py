# O(N)
# https://www.youtube.com/watch?v=f6ct5PQHqM0

s = input()

def z_algo(s):
    n = len(s)
    A = [0] * n
    A[0] = n
    fr = -1
    last = -1
    for i in range(1, n):
        same = 0
        # 現在見ているiがfrからlastの間に入っていた場合、
        # 前回frとlastを更新した時ににすでに探索されているので
        # A[1]からA[last-fr]までの配列の再利用を検討
        if fr != -1:
            # A[i-fr] > last-iの場合、same=last-i -> i+same=lastとなり、
            # lastまでは一致していることが保証されるがlast以降はわからない
            # 後はsameがどこまで伸ばせるか、まだ未探索のlast以降を調べる

            # A[i-fr] < last-iの場合、今見ているiの伸ばせる範囲がlast未満で
            # あることが確定するので、A[i] = A[i-fr]となる
            # なので下のwhileループは回らないはず？
            same = min(A[i-fr], last-i)

            # last-iが負、つまりiがlastを超えて新たに探索を始めた場合を
            # 場合分けする代わりに、0とmaxを取ることで場合分けと同等の処理をしている
            # つまり same = max(0, same)　は  if last < i -> same = 0　と同じ
            same = max(0, same)
        while i + same < n and s[same] == s[i+same]:
            same += 1
        A[i] = same
        if last < i + same:
            last = i + same
            fr = i
    return A

print(z_algo(s))