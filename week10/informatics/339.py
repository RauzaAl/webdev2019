x = int(input())
y = 0
for i in range(2,x+1):
	if x%i==0:
		y=i
		break
print(y)