import bisect

ranges_left = []
ranges_right = []

f = open("input.txt", "r")

while True:
    l = f.readline().strip()
    if l == '': 
        break
    s, e = map(int, l.strip().split('-'))

    i = bisect.bisect_left(ranges_right, s)
    j = bisect.bisect_right(ranges_left, e)

    if i < j:
        s = min(s, ranges_left[i])
        e = max(e, ranges_right[j - 1])

    ranges_left[i:j] = [s]
    ranges_right[i:j] = [e]

total = 0 
for i in range(len(ranges_left)):
    total += ranges_right[i] - ranges_left[i] + 1
print(total)