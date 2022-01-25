"""
	Q) _ (underscore)의 사용 관례?

"""

## tuple packing
tri_one = (12, 15)
tri_two = 23, 12

## tuple unpacking
bt, ht = tri_one

nums = (1, 2, 3, 4, 5)
n1, n2, *others = nums
print(others)

first, *others, last = nums
print(others)

## tuple packing in function call
def ref_nums():
	return 1, 2, 3, 4, 5

nums = ref_nums()
print(nums)

n, *others = ref_nums()
print(others) ## list

def show_nums(n1, n2, *others):
	print(n1, n2, others) ## others : tuple

show_nums(1, 2, 3, 4)
show_nums(1, 2, 3, 4, 5)

def sum(*nums):
	s = 0
	for i in nums:
		s += i
	return s

sum(1,2,3)
sum(1,2,3,4,5)

## tuple unpacking in function call
def show_man(name, age, height):
	print(name, age, height)

p = ('Yoon', 22, 180)
show_man(*p)

## complex tuple unpacking
t = (1, 2, (3, 4))
a, b, (c, d) = t
print(a, b, c, d)

p = 'Hong', (32, 178), '010-1234-56xx', 'Korea'
na, (ag, he), ph, ad = p
na, (_, he), _, _ = p

## unpacking in for loop
ps = [('Lee', 172), ('Jung', 182), ('Yoon', 179)]
for n, h in ps:
	print(n, h)
