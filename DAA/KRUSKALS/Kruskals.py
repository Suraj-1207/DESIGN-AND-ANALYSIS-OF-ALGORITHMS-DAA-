class Union_Find:
	def __init__(self):
		self.n = int(input("Enter the no of vertices: "))
		self.m = int(input("Enter the no of edges: "))
		self.adj = []
		print("Enter the edges in the form wt,u,v ")
		for i in range(self.m):
			self.adj.append(list(map(int,input().split())))
		self.pt = [-1 for i in range(self.n+1)]
		self.sz = [1 for i in range(self.n+1)]

	def find(self,u):
		if(self.pt[u] == -1): return u
		self.pt[u] = self.find(self.pt[u])
		return self.pt[u]

	def union(self,u,v):
		if self.sz[u] > self.sz[v]: u,v = v,u # path compression
		self.pt[u] = v
		self.sz[v] += self.sz[u]
	
	def Kruskals(self):
		self.adj.sort()
		
		total_wt = 0
		mst = []
		
		for it in self.adj:
			u = it[1]
			v = it[2]
			a = self.find(u)
			b = self.find(v)
			if(a != b):
				self.union(a,b)
				total_wt += it[0]
				mst.append(it)
		
		print("Total weight :",total_wt)
		print("Edges forming the MST : ")	
		for i in mst:
			print("w,u,v :",i)	

DSU = Union_Find()
DSU.Kruskals()

'''
Output : 
n = 5
m = 10
Edges:
3 1 2
5 1 4
15 1 3
6 1 5
7 2 3
4 2 4
9 2 5
10 3 4
11 3 5
1 4 5
Total weight : 15
Edges forming the MST : 
w,u,v : [1, 4, 5]
w,u,v : [3, 1, 2]
w,u,v : [4, 2, 4]
w,u,v : [7, 2, 3]
'''
