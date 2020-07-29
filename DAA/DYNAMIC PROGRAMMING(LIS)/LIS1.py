def LIS(a, dp):
	for i in range(len(a)):
		for j in range(i+1):
			if(a[j]<a[i]): 
				if(dp[j]+1>dp[i]):
					dp[i]=dp[j]+1
				
a=list(map(int, input("Enter an array: ").split()))
dp=[1 for i in range(len(a))]
LIS(a,dp)
#print(dp[len(a)-1])
res=-(1<<32)
for i in range(len(a)-1):
	res=max(res, dp[i])
print(res)



