<<<<<<< HEAD
n = int(input())
s = input().split(' ')
count=0
for i in range(0,n-2):
    if int(s[i+1])>int(s[i]) and  int(s[i+1])>int(s[i+2]):
        count =count+1
=======
n = int(input())
s = input().split(' ')
count=0
for i in range(0,n-2):
    if int(s[i+1])>int(s[i]) and  int(s[i+1])>int(s[i+2]):
        count =count+1
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
print(count)