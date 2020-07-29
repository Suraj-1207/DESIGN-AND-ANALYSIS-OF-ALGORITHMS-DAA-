def mss(a):
	n=len(a)
	rsum=0
	finsum=-100000000	
	for i in range(n):
		rsum+=a[i]
		rsum=max(rsum, 0)
		finsum=max(finsum, rsum)
	return finsum

print("Enter an Array: ")
a=list(map(int, input().split(" ")))

res=mss(a)
print("Sum is: ", res)
