nuts=list(map(int, input("Enter NUTS array: ").split()))
bolts=list(map(int, input("Enter BOLTS array: ").split()))
for i in range(len(nuts)):
	for j in range(len(bolts)):
		if(nuts[i]==bolts[j]):
			print(nuts[i], "matches with", bolts[j])
			
