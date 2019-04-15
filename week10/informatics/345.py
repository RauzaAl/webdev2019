<<<<<<< HEAD
a=[]
n=int(input())
count=0
for i in range(n):
	new=int(input())
	a.append(new)
for i in range(n):
	if a[i]==0:
		count= count+1
=======
a=[]
n=int(input())
count=0
for i in range(n):
	new=int(input())
	a.append(new)
for i in range(n):
	if a[i]==0:
		count= count+1
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
print(count)