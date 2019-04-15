<<<<<<< HEAD
n = int(input())
s = input().split(' ')
count=True
for i in range(0,n-1):
    if (int(s[i+1])> 0 and int(s[i])>0) or  (int(s[i+1])< 0 and int(s[i])<0):
        count = False
if count==False:
    print("YES")
else:
=======
n = int(input())
s = input().split(' ')
count=True
for i in range(0,n-1):
    if (int(s[i+1])> 0 and int(s[i])>0) or  (int(s[i+1])< 0 and int(s[i])<0):
        count = False
if count==False:
    print("YES")
else:
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
    print("NO")