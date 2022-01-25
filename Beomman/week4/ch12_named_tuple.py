from collections import namedtuple

"""
	namedtuple 실제 코딩시 활용에 대한 생각:
	
	tuple이나 list는 여러 개의 연관된 정보를 저장하기 위한 데이터 타입..
	예를 들어, 코딩하다 보면 [('chr1', 1000, 1500, 'A', 'G'), ...] 이런식으로 연관된 정보를 tuple, list로 활용하여 저장하는 경우가 많음
	이때, 정보를 속성으로 두고 저장하는 정보 저장용(?) 클래스를 만들어서 처리해야하는 고민이 있었는데, 이럴 경우에 namedtuple 활용도가 높을 것 같음.

	Q1) namedtuple의 속성을 추가할 수 있나?? -> X
	Q2) tuple과 namedtuple의 메모리 차이?? -> memory size diff X

"""

## namedtuple example
Tri = namedtuple('Triangle', ['bottom', 'height'])
t = Tri(7, 8)
#t.test = 9 ## Error
print(t)
print(t.bottom, t.height)

## namedtuple unpacking
Tri = namedtuple('Tri', ['bottom', 'height'])  ## recommended 
Tri = namedtuple('Tri', 'bottom height')

t = Tri(12, 79)
a, b = t
print(a, b)

tt = Tri(bottom=12, height=79)  ## another method
print(tt)

def show(n1, n2):  ## unpacking in function call
	print(n1, n2)
show(*t)

## Memory size comparison to default tuple
import sys

Variant = namedtuple('Variant', 'chrom pos ref_allele alt_allele gene effect dbsnp135 dbsnp154')
v = Variant('chr1', 1000, 'A', 'G', 'BM', 'synonymous', 'rs000000', 'rs111111')
print(v)
print(sys.getsizeof(v))

chrom, pos, ref, alt, *_ = v  ## unpacking
print(chrom, pos, ref, alt, _)

vv = ('chr1', 1000, 'A', 'G', 'BM', 'synonymous', 'rs000000', 'rs111111')
print(vv)
print(sys.getsizeof(vv))
