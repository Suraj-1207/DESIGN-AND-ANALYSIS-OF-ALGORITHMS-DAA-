def mss(a, lo, hi):
	if(hi==lo):
		return a[lo]
	
	mid=(lo+hi)//2
	lsum=rsum=-100000000
	ss=0
	for i in range (mid,lo-1,-1):
		ss+=a[i]
		lsum=max(lsum,ss)
	
	ss=0
	for i in range (mid+1,hi+1):
		ss+=a[i]
		rsum=max(rsum,ss)

	return max(mss(a,lo,mid), mss(a,mid+1,hi), lsum+rsum)

print("Enter an Array: ")
a=list(map(int, input().split(" ")))

res=mss(a, 0, len(a)-1)
print("Sum is: ", res)
