# Sを90°回転, 2回適応で180°、3回で270°

def rot(S):
	return list(zip(*S[::-1]))

N = int(input())
S = [list(input()) for _ in range(N)]

print(rot(S))