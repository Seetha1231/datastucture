#in undirected graph
from collections import defaultdict 
class graph:
	def __init__(self,vertices):
		self.v=vertices
		self.graph=defaultdict(list)
	def addEdge(self,u,v):
		self.graph[u].append(v)
	def find(self,parent,i):
		if parent[i]==-1:
			return i
		return self.find(parent,parent[i])
	def union(self,parent,x,y):
		xset=self.find(parent,x)
		yset=self.find(parent,y)
		parent[xset]=yset
	def isCycle(self):
		parent=[-1]* (self.v)
		for i in self.graph:
			for j in self.graph[i]:
				x=self.find(parent,i)
				y=self.find(parent,j)
				if x==y:
					return 1
				self.union(parent,x,y)
def main():
	v=int(input('Enter no of Vertices :'))
	g=graph(v)
	e=int(input('Enter no of Edges :'))
	for i in range(e):
		g.addEdge(int(input('Enter edge 1:')),int(input('Enter edge 2:')))
	check=g.isCycle()
	if check==1:
		print('Cycle Exist ')
	else :
		print('No Cycle ')
main()
