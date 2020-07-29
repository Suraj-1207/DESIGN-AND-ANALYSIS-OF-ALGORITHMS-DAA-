def max_subarray_sum_cubic(a):
	ans=0
	for i in range(len(a)):
		for j in range(len(a)):
			sum=0
			for k in range(i,j+1):
				sum+=a[i]
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


				
