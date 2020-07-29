def partition(a, lo, hi):
	i=lo
	j=lo
	piv=a[hi]
	while(j<hi):
		if a[j]<piv:
			a[i],a[j]=a[j],a[i]
			i+=1
		j+=1
	a[i],a[hi]=a[hi],a[i]
	return i

def quicksort(a,l,r):
	if(l<r):
		j=partition(a,l,r)
		quicksort(a,l,j-1)
		quicksort(a,j+1,r)
	
nuts=list(map(int, input("Enter NUTS array: ").split()))
bolts=list(map(int, input("Enter BOLTS array: ").split()))
quicksort(nuts,0,len(nuts)-1)
quicksort(bolts,0,len(bolts)-1)

for i in range(len(nuts)-1):
	print(nuts[i], "matches with", bolts[i])

			
