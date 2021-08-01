from collections import deque

N = int(input())

ans = 0

# キューを用意
Q = deque()
Q.append(0)

# キューから取り出しながら探索する
while len(Q) > 0:
    i = Q.popleft()
    for j in [3, 5, 7]:
        n = 10*i+j

        if n > N:
            continue
        if "3" in str(n) and "5" in str(n) and "7" in str(n):
            ans += 1

        Q.append(n)

print(ans)