<<<<<<< HEAD
n = int(input())
s = input().split(' ')
count=0
for i in range(1,n):
    if int(s[i])>int(s[i-1]):
        count+=1
=======
n = int(input())
s = input().split(' ')
count=0
for i in range(1,n):
    if int(s[i])>int(s[i-1]):
        count+=1
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
print(count)