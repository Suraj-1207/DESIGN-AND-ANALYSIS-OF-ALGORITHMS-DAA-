class DiGraph:
	def __init__ (self):
		self.n = int(input("Enter the no of vertices : "))
		self.adj_matrix=[[0 for i in range(self.n)]for j in range(self.n)]
		for i in range(self.n):
			for j in range(self.n):
				if(i != j):
					self.adj_matrix[i][j] = 1e9

		self.m = int(input("Enter the no of edges : "))

		for i in range(self.m):
			u,v,w=map(int,input().split())
			self.adj_matrix[u][v] = w

class MinHeap:
	def __init__(self):
		self.n=0
		self.arr=[[-1,-1]]


	def sink (self, i):
		while(self.n >= 2*i + 1):
			if(self.arr[i][1]<=self.arr[2*i][1] or self.arr[i][1] <= self.arr[2*i +1][1]):
				if (self.arr[2*i][1] >= self.arr[2*i+1][1]):
					self.arr[i], self.arr[2*i+1] = self.arr[2*i +1], self.arr[i]
					i=2*i+1
				else:
					self.arr[i], self.arr[2*i] = self.arr[2*i], self.arr[i] 
					i=2*i

	def swim (self, i):
		while(self.arr[i][1] < self.arr[i//2][1]):
			self.arr[i], self.arr[i//2] = self.arr[i//2], self.arr[i]
			i//=2

	def Insert (self, i, k):
		self.n+=1
		self.arr.append([i,k])
		self.swim(self.n)

	def DeleteMin(self):
		self.arr[1], self.arr[self.n]=self.arr[self.n],self.arr[1]
		x=self.arr.pop()
		self.n-=1
		self.sink(1)
		return x

	def DecreaseKey(self,i, x, k):
		if (i>self.n):
			return

		if(self.arr[i][0]==x):
			self.arr[i][1]=k
			self.swim(i)
			return

		self.DecreaseKey(2*i, x, k)
		self.DecreaseKey(2*i+1, x, k)

	def isEmpty(self):
		if self.n == 0:
			return True
		return False

	def print(self, i, spacing):
		if (i>self.n):
			return
		print(spacing, end=" ")
		if (i==1):
			print(self.arr[i])
		elif(i%2):
			print("L - - - ",self.arr[i])
			spacing += "|			 "
		else:
			print("R - - - ",self.arr[i])
			spacing += "			 "
		self.print(2*i, spacing)
		self.print(2*i+1, spacing)

class SP:
	def __init__ (self, source):
		self.source = source
		self.H = MinHeap()
		self.G = DiGraph()
		self.distance = []
		self.is_in_MinHeap = []
		self.prev = [-1 for i in range (self.G.n)]
		self.H.Insert(source,0)
		for i in range (self.G.n):
			if(i==source):
				self.distance.append(0)
				self.is_in_MinHeap.append(True)
			else:
				self.distance.append(1e9)
				self.is_in_MinHeap.append(False)

	def Relax(self, u , v):
		self.distance[v] = self.distance[u] + self.G.adj_matrix[u][v]

	def is_Tense(self, u, v):
		return  self.distance[v] > self.distance[u] + self.G.adj_matrix[u][v]

	def Djikstras(self):
		while (not self.H.isEmpty()):
			u,dist = self.H.DeleteMin()
			self.is_in_MinHeap[u]=False
		
			for v in range(self.G.n):
				if(u != v and self.G.adj_matrix[u][v] != 1e9):
					if (self.is_Tense(u,v)):
						self.Relax(u,v)
						self.prev[v]=u
						if(self.is_in_MinHeap[v]):	self.H.DecreaseKey(v,self.distance[v],1)
						else:
							self.H.Insert(v, self.distance[v])
							self.is_in_MinHeap[v]=True

	def paths(self):
		for i in range (self.G.n):
			if(i==self.source):
				continue

			print("Distance from source ", self.source, " to vertex ", i, ": ", self.distance[i])
			print("Path from source : ",end=" ")

			p = [str(i)]
			j = self.prev[i]
			while(j != -1):
				p.append(str(j))
				j = self.prev[j]
			p = p[::-1]
			print('->'.join(p))

sssp = SP(0)
sssp.Djikstras()
sssp.paths()

'''
Output:
Enter the no of vertices : 4
Enter the no of edges : 5
0 2 10
0 1 4
1 2 2
2 3 5
1 3 6
Distance from source  0  to vertex  1 :  4
Path from source :  0->1
Distance from source  0  to vertex  2 :  6
Path from source :  0->1->2
Distance from source  0  to vertex  3 :  10
Path from source :  0->1->3
'''
