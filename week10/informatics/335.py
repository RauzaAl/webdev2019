import math
a = int(input())
b = int(input())
for i in range(a, b+1):
	j = (math.sqrt(1.0*i))
if j*j==1:
	print(i)