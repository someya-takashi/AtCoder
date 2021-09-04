
data = []
for i in range(409):
    A = input()
    a = A[:4]
    b = A[7:16]
    data.append([a, b])

for i in range(409):
    print(data[i][0], data[i][1])
