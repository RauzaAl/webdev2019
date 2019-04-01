n = int(input())
bitAmount=0
while n:
	bitAmount += n%2
	n/=2
	break
if bitAmount==1:
	print("YES")
else: 
	print("NO")