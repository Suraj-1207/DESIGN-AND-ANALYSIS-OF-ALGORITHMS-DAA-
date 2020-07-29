def LIS(a, dp, prev):
	for i in range(len(a)):
		for j in range(i+1):
			if(a[j]<a[i]): 
				if(dp[j]+1>dp[i]):
					dp[i]=dp[j]+1
					prev[i]=j+1
				
a=list(map(int, input("Enter an array: ").split()))
dp=[1 for i in range(len(a))]
prev=[i+1 for i in range(len(a))]
LIS(a,dp,prev)
print("DP: ", dp)
print("PREV: ", prev)



