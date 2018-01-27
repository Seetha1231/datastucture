class queue :
	def __init__(self):
		self.ar=[]
	def enqueue(self,n):
		self.ar.insert(0,n)
		return len(self.ar)
	def dequeue(self):
		try:
			return (self.ar.pop(),len(self.ar))
		except IndexError:
			return (-1,0)
