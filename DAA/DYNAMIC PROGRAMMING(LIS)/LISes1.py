def LIS(a,b,c):
	sz=0
	fin=[]
	n=len(a)
	for mask in range(1<<n):
		arr=[]
		for j in range(n):
			if mask & (1<<j):
				arr.append(a[j])
			
		ne, ok=len(arr),1
		for i in range(1,ne):
			if(arr[i]<arr[i-1]):
				ok=0;
				break
		if ok==1 and ne>=sz:
			sz=max(sz,ne)
			sz=ne
			fin=[]
			fin=arr[:]
		
	b[n-1]=sz
	c[n-1]=fin[:]
	
def driver(a,b,c):
	for i in range(len(a)): LIS(a[:i+1],b,c)
	print(c)
	print(b)
		
a=list(map(int, input("Enter an array: ").split()))
b=[0 for i in range(len(a))]
c=[[] for i in range(len(a))]
driver(a,b,c);
#print(res, " length=", len(res))
