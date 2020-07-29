def inverseCount(arr):
	return mergeSort(arr,0,len(arr)-1)

def merge(arr, l, m, r): 
	ct=0
	L=arr[l:m+1]
	R=arr[m+1:r+1]
	n1=len(L)
	n2=len(R) 
	
	i=j=0
	k=l
 
	while (i<n1 and j<n2): 
		if (L[i]<=R[j]): 
			arr[k]=L[i] 
			i+=1   
		else:	
			ct+=(m+1)-(i+l)
			arr[k]=R[j]
			j+=1 
		k+=1
    
	while (i<n1): 
		arr[k]=L[i] 
		i+=1 
		k+=1 
    	 
  
	while (j<n2): 
		arr[k]=R[j] 
		j+=1
		k+=1
		
	return ct
     
def mergeSort(arr, l, r): 
	ct=0
	if (l<r): 
		m = (l+r)//2; 
		ct+=mergeSort(arr, l, m)
		ct+=mergeSort(arr, m+1, r)
		ct+=merge(arr, l, m, r)
	return ct
  
a=list(map(int, input("Enter an array: ").split(" ")))
print ("The inversion count is:  ", inverseCount(a))

'''
Output:
Enter an array: 1 20 6 4 5
The inversion count is:  5
'''


