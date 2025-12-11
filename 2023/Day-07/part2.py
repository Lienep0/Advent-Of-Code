from collections import Counter
from functools import cmp_to_key

ranks = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def category(hand):
    c = Counter(hand)

    if "J" in hand :
        best_c = max(c.keys(), key=lambda x: c[x])
        if best_c == "J":
            if len(c) == 1:
                return 6
            c_copy = c.copy()
            del c_copy["J"]
            best_c_copy = max(c_copy.keys(), key=lambda x: c_copy[x])
            c[best_c_copy] = c[best_c_copy] + c["J"]
        else:
            c[best_c] = c[best_c] + c["J"]
    del c["J"]
    counts = sorted(c.values(), reverse=True)
    
    if counts == [5]:
        return 6
    elif counts == [4, 1]:
        return 5
    elif counts == [3, 2]:
        return 4
    elif counts == [3, 1, 1]:
        return 3
    elif counts == [2, 2, 1]:
        return 2
    elif counts == [2, 1, 1, 1]:
        return 1
    else:
        return 0
    
def comparaison(a1, a2):
    """
    returns -1 if a1 < a2
    returns 1 if a1 > a2
    """
    hand1, _ = a1
    hand2, _ = a2
    c1 = category(hand1)
    c2 = category(hand2)
    if c1 != c2:
        if c1 < c2:
            return -1
        return 1
    else:
        i = 0
        while hand1[i] == hand2[i]:
            i += 1
        r1 = ranks.index(hand1[i])
        r2 = ranks.index(hand2[i])
        if r1 < r2:
            return -1
        return 1

with open("input.txt", "r") as f:
    hands = [(a, int(b)) for a, b in [line.strip().split(' ') for line in f.readlines()]]
    sorted_hands = sorted(hands, key=cmp_to_key(comparaison))

total = 0
for i, hand in enumerate(sorted_hands):
    _, score = hand
    total += score * (i + 1)
print(total)