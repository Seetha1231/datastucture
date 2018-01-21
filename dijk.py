class graph:
	def __init__(self,vertices):
		self.v=vertices
		self.graph=[[0 for i in range(vertices)] for j in range(vertices)]
	def addEdge(self,u,v,w):
		self.graph[u][v]=w
		self.graph[v][u]=w
	def mindistance(self,dist,shset):
		min=9999
		min_index=1
		for i in range(self.v):
			if dist[i]<min and shset[i]==False :
				min=dist[i]
				min_index=i
		return min_index
	def dijkstra(self,src):
		dist=[9999]*self.v
		dist[src]=0
		shset=[False]*self.v
		for count in range(self.v):
			u=self.mindistance(dist,shset)
			shset[u]=True
			for i in range(self.v):
				if self.graph[u][i]>0 and shset[i]==False and dist[i]>dist[u]+self.graph[u][i]:
					dist[i]=dist[u]+self.graph[u][i]
		self.print(dist)
	def print(self,dist):
		print("Vertex \t Distance from Source")
		for i in range(self.v):
			print(i,"\t",dist[i])

def main():
	v=int(input('Enter no of Vertices :'))
	g=graph(v)
	e=int(input('Enter no of Edges :'))
	for i in range(e):
		g.addEdge(int(input('Enter edge 1:')),int(input('Enter edge 2:')),int(input('Enter weight :')))
	g.dijkstra(int(input('Enter Source :')))
main()