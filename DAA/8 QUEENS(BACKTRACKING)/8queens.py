ct = 0
def check(ans):
	n = len(ans)-1
	s = ans[n]+n
	for j in range(n):
		if(ans[j]+j == s): return False
	d = ans[n]-n
	for j in range(n):
		if(ans[j]-j == d): return False
	return True
	
def recursol(vis,ans,ind):
	global ct
	if ind == 8:
		ct += 1
		print("Solution",ct,":")
		for i in range(8):
			coordinate = (i+1,ans[i])
			print(coordinate)
		return
	for i in range(8):
		if(vis[i] == 0):
			vis[i] = 1
			ans.append(i+1)
			if check(ans) == True: recursol(vis,ans,ind+1) 
			ans.pop() 
			vis[i] = 0

recursol([0 for i in range(8)],[],0)
print("Total no of solutions : ",ct)
