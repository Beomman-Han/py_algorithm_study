"""
Solution
	direction: (+) or (-)
	At the end of square, direction must be changed.

"""

X = int(input())
row = 0
col = 0
direction = 1
for i in range(X-1):
	if row == 0 and col == 0:
		col += 1
		direction *= -1
	elif row == 0:
		if direction == -1:
			row += 1
			col -= 1
		else:
			col += 1
			direction *= -1
	elif col == 0:
		if direction == -1:
			row += 1
			direction *= -1
		else:
			row -= 1
			col += 1
	else:
		if direction == -1:
			row += 1
			col -= 1
		else:
			row -= 1
			col += 1
print(f'{row+1}/{col+1}')
