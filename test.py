A, B = map(int, input().split())

for i in range(100000):
    a = (i * 0.08)//1
    b = (i * 0.1)//1
    if a == A and b == B:
        print(i)
        exit()

print(-1)