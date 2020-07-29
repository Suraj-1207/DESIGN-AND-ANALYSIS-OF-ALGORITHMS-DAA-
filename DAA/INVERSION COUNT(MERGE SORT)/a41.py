def inverseCount(a):
	res=0
	n=len(a)
	for i in range (n):
		for j in range (i+1,n):
			if(a[i]>a[j]):
				res+=1
	return res

a=list(map(int, input("Enter an array: ").split(" ")))
print ("The inversion count is:  ", inverseCount(a))


