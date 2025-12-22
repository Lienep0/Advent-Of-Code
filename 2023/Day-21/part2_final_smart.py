N = 26501365 // 131
N = 2

X = 3503
X_ = 3606
Y = 3689.5
Y_ = 3476

X_formula = ((N + 1) - (N % 2)) ** 2
X__formula = (N + (N % 2)) ** 2
Y_formula = Y__formula = (4 * N) - 2 if N != 0 else 0

print(X * X_formula + X_ * X__formula + Y * Y_formula + Y_ * Y__formula)

# 590_309_300_938_806 : too high
# 290_945_141_077_282 : too low
# 290_986_027_525_574 : too low
# 290_988_945_543_858 : no