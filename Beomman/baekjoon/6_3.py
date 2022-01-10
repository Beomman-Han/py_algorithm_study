def is_hansoo(num: int) -> bool:
	"""Check input number is hansoo.
	hansoo: a number where each digit number forms arithmetic sequence
	Ex) 1, 321, 531, 1062(X)
	
	Parameters
	----------
	num: int
		input number
	
	Returns
	-------
	bool
		is input number hansoo
	"""

	str_num = str(num)
	if len(str_num) == 1:
		return True

	prev_diff = int(str_num[-2]) - int(str_num[-1])
	for digit in range(len(str_num)-1):
		prev_idx = -1*digit+len(str_num)-2
		curr_idx = -1*digit+len(str_num)-1
		diff = int(str_num[prev_idx]) - int(str_num[curr_idx])
		if diff != prev_diff:
			return False
		prev_diff = diff
	return True

def main():
	N = int(input())
	count = 0
	for i in range(N):
		if is_hansoo(i+1):
			count += 1
	print(count)
main()
