STEPS = 26501365
l = 131
N = STEPS // l

N = 1

tiles_OE = 3582
tiles_EE = 3582
tiles_OC = 3606
tiles_EC = 3503

card_I = (N + 1 - (N % 2)) ** 2
card_O = (N + (N % 2)) ** 2
card_X = card_D = (4 * N) - 2 if N != 0 else 0

total = card_I * tiles_OC + card_O * tiles_EC + card_X * tiles_OE + card_D * tiles_EE
print(total)

# 590_309_300_938_806 : too high
# 290_945_141_077_282 : too low
# 290_986_027_525_574 : too low