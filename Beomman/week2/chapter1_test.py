import sys

## reference counting practice

a = 'garbage collection'
print(sys.getrefcount(a))  ## Why 4?

b = a
print(sys.getrefcount(a))

class test(object):
	def __init__(self):
		pass

a = test()
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(a))

## garbage collection practice

import gc

print(gc.get_threshold())
print(gc.get_count())
gc.collect()
print(gc.get_count())
gc.set_threshold(1000, 15, 15)
