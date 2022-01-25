"""
	String formatting expressions
"""

s = 'My friend %s is %d years old and %fcm tall.' %('Jung', 22, 178.5)
print(s)

#s = 'My friend %d is %d years old and %dcm tall.' %('Jung', 22, 178.5)  ## impossible

s = 'My friend %s is %s years old and %scm tall.' %('Jung', 22, 178.5)  ## possible
print(s)

s = "%(name)s : %(age)d" %{'name': 'Yoon', 'age': 22}
print(s)

s = '%(name)s : %(age)d' %{'name': 'Yoon', 'age': 22}
print(s)

#s = "%(name)s : %(age)d" %{name: 'Yoon', age: 22}  ## impossible

s = 'height: %.3f' % 3.14
print(s)

s = 'height: %.2f' % 3.14
print(s)

s = 'height: %7.2f' % 3.14
print(s)

s = 'height: %07.2f' % 3.14
print(s)
s = 'height: %-7.2f' % 3.14
print(s)
s = 'height: %+7.2f' % 3.14
print(s)

s = '%(h)s: %(v)-+10.3f입니다.' %{'h': 'height', 'v': 3.14}
print(s)

"""
	String formatting method calls
"""

s = '{0}...{1}...{2}'.format('Robot', 125, 'Box')
print(s)
s = '{}...{}...{}'.format('Robot', 125, 'Box')
print(s)
s = '{2}...{0}...{1}'.format('Robot', 125, 'Box')
print(s)

## key: value
s = '{toy}...{num}...{item}'.format(toy = 'Robot', num = 125, item = 'Box')
print(s)

## with unpacking
my = ['Robot', 125, 'Box']
s = '{}...{}...{}'.format(*my)
print(s)

my = ['Box', (24, 31)]
s = '{0[0]}...{0[1]}...{1[0]}...{1[1]}'.format(*my)
print(s)

d = {'toy': 'Robot', 'price': 3500}
d2 = {'item': 'Box'}
s = 'toy = {0[toy]}, price = {0[price]}, item = {1[item]}'.format(d, d2)
print(s)

s = '{0:.4f}'.format(3.14)
print(s)
s = '{0:9.4f}'.format(3.14)
print(s)
s = '{0:<10.4f}'.format(3.14)
print(s)
s = '{0:>10.4f}'.format(3.14)
print(s)
s = '{0:^10.4f}'.format(3.14)
print(s)
s = '{:^10.4f}'.format(3.14)
print(s)

s = '{:*^10.4f}'.format(3.14)
print(s)
s = '{:+>+10.4f}'.format(3.14)
print(s)
s = '{:+<10.4f}'.format(3.14)
print(s)
s = '{:+<+10.4f}'.format(3.14)
print(s)
s = '{:^^10.4f}'.format(3.14)
print(s)
