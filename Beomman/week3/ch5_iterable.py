"""
class vcf_viewer(object):
	def __init__(vcf_: str) -> None:
		self.vcf_ = vcf_
	
	def open(self):
		self.vcf = open(self.vcf_, 'r')
		return

	def close(self):
		self.vcf.close()
		return

	def __iter__(self):
		return self
	
	def __next__(self):
		return
"""

class counter(object):
	"""Iterator, Iterable object practice class

	Methods
	-------
	__iter__
	__next__
	"""

	def __init__(self, low, high):
		
		self.low = low
		self.high = high

		self.current = low - 1
		self.high    = high

		return

	def __iter__(self):
		
		if self.current < self.high:
			return self
		else:
			self.__init__(self.low, self.high)
			return self
	
	def __next__(self):
		self.current += 1
		if self.current < self.high:
			return self.current
		else:
			raise StopIteration
