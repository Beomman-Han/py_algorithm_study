case_num = int(input())

for i in range(case_num):
	[A, B] = [int(x) for x in input().strip().split()]
	print(f'Case #{i+1}: {A} + {B} = {A+B}')
