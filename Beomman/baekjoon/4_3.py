"""
Ex)
	26->68->84->42->26
	4 cycle
"""

N = input()

if len(N) == 1:
	N = '0' + N

prev_N = N
new_N = None
cycle = 0
while new_N != N:
	if len(prev_N) == 1:
		prev_N = '0' + prev_N
	new_N = sum([int(x) for x in prev_N])
	new_N = str(prev_N)[-1] + str(new_N)[-1]
	prev_N = new_N
	cycle += 1
print(cycle)
