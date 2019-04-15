<<<<<<< HEAD
def count_code(str):
  count = 0
  i=0
  while "co" in str[i:]:
    if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
      count += 1
    i += str[i:].index("co")+3
  return count
=======
def count_code(str):
  count = 0
  i=0
  while "co" in str[i:]:
    if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
      count += 1
    i += str[i:].index("co")+3
  return count
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
