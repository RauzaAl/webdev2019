<<<<<<< HEAD
def xyz_there(str):
  i=0
  while "xyz" in str[i:]:
    if str[i-1+str[i:].index("xyz")] != ".":
      return True
    i += str[i:].index("xyz")+2
  return False
=======
def xyz_there(str):
  i=0
  while "xyz" in str[i:]:
    if str[i-1+str[i:].index("xyz")] != ".":
      return True
    i += str[i:].index("xyz")+2
  return False
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
