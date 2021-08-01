from itertools import permutations

N = int(input())
k = int(input())

cards = [int(input()) for _ in range(N)]

card_num = set()
for p in permutations(cards, k):
    value = ""
    for card in p:
        value+=str(card)

    card_num.add(value)

print(len(card_num))
