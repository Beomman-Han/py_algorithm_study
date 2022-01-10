[x, y, w, h] = [ int(e) for e in input().strip().split() ]

print(min(abs(x), abs(y), abs(x-w), abs(y-h)))
