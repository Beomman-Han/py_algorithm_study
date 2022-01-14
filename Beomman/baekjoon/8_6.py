""" Recursive method
def rule(floor: int, room: int) -> int:
	if floor == 0:
		return room
	
	return
"""

T = int(input())
for i in range(T):
	floor = int(input())
	room = int(input())
	
	resident_nums = [i+1 for i in range(room)]
	for k in range(floor):
		for n in range(1, room):
			resident_nums[n] += resident_nums[n-1]
	print(resident_nums[-1])
