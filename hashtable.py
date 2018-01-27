class Hashmap:
	def __init__(self,size):
		self.size=size
		self.map=[None]*self.size
	def get_hash(self,key):
		hash=key
		return (hash-1)%self.size
	def add(self,key,value):
		key_hash=self.get_hash(key)
		key_value=[key,value]
		pair=[]
		if self.map[key_hash] is None :
			self.map[key_hash]=list(key_value)
			return True
		else :
			for pair in self.map[key_hash]:
				if pair[0]==key:
					pair[1]=value
					return True
				self.map[key_hash].append(key_value)
				return True
	def get(self,key):
		key_hash=self.get_hash(key)
		pair=[]
		try:
			return self.map[key_hash][1]
		except:
			return None
			
n=int(input())
hash=Hashmap(n)
for i in range(n):
    key,value=map(str,input().split())
    hash.add(int(key),value)
q=int(input())
for i in range(q):
    x=int(input())
    print(hash.get(x))
        
