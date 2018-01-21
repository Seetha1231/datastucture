class graph:
	def __init__(self,vertices):
		self.v=vertices
		self.graph=[]
	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])
	def find(self,parent,i):
		if parent[i]==i:
			return i
		return self.find(parent,parent[i])
	def union(self,parent,rank,x,y):
		xset=self.find(parent,x)
		yset=self.find(parent,y)
		if rank[xset]<rank[yset]:
			parent[xset]=yset
		elif rank[yset]<rank[xset]:
			parent[yset]=xset
		else :
			parent[yset]=xset
			rank[xset]+=1

	def kruskalMST(self):
		result,parent,rank=[],[],[]
		i,e=0,0
		self.graph = sorted(self.graph,key=lambda item: item[2])
		for node in range(self.v):
			parent.append(node)
			rank.append(0)
		while e<self.v-1:
			u,v,w=self.graph[i]
			i=i+1
			x=self.find(parent,u)
			y=self.find(parent,v)
			if x!=y:
				result.append([u,v,w])
				e+=1
				self.union(parent,rank,x,y)
		print('\nMinimum Spanning Tree :')
		for u,v,w in result :
			print(str(u) +'---'+str(v)+'='+str(w))
def main():
	v=int(input('Enter no of Vertices :'))
	g=graph(v)
	e=int(input('Enter no of Edges :'))
	for i in range(e):
		g.addEdge(int(input('Enter edge 1:')),int(input('Enter edge 2:')),int(input('Enter weight :')))
	g.kruskalMST()
main()