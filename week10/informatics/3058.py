a = int(input())
n = 0
for i in range(2, a+1):
	if a%i==0:
		n=i
		break
print(n)