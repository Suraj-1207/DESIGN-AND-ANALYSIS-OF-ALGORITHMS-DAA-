def max_subarray_sum_cubic(a):
	ans=0
	pre=[0 for i in range(len(a))]
	pre[0]=a[0]
	for i in range(1,len(a)):
		pre[i]=pre[i-1]+a[i]
	for i in range(len(a)):
		for j in range(len(a)):
			if(i==0):
				sum=pre[j]
			elif(j>=i):
				sum=pre[j]-pre[i-1]
			if(sum>ans):
				l=i
				m=j
				ans=sum
	print("array elements added are:")
	for i in range(l,m+1):
		print(a[i])
	print("maximum sum of subarray is:",ans)

n=int(input("Enter number of elements:"))
arr=[int(input("enter no:")) for i in range(n)]
max_subarray_sum_cubic(arr)


				
