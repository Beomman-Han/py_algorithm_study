"""
Solution
	Iterate reverse string of input2 ('485'->'584') and multiply with input1 integer.

Ex)

	input1 : '375' -> 375 (int)
	input2 : '485' -> '584' (str)

	(1) 375 * 5 -> print
	(2) 375 * 8 -> print
	(3) 375 * 4 -> print

	(1) + ((2) * 10) + ((3) * 100) -> print
"""

input_1 = input()
input_2 = input()

result = 0
for digit in range(len(input_2)):
	num_1 = int(input_1)
	num_2 = int(input_2[::-1][digit])
	print(num_1 * num_2)
	result += (num_1 * num_2 * (10 ** digit))
print(result)
