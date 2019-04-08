x = int(input())
k = 2
for i in range(2,x):
	if x%i==0:
		k=k+1
print(k)