<<<<<<< HEAD
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]
  return str[len(str)-1] + mid + str[0]
=======
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]
  return str[len(str)-1] + mid + str[0]
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
 #замена первого и последнего символа местами