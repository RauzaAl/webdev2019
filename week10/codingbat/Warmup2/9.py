def string_match(a, b):
  def splitter(str,n):
    result = []
    for i in range(0,len(str)-n+1):
      result.append(str[i:i+n])
    return result
    
  count = 0
  a_split = splitter(a,2)
  b_split = splitter(b,2)
  
  for i in range(0, len(a_split) if len(a_split)<=len(b_split) else len(b_split)):
    if a_split[i] == b_split[i]:
      count += 1
      
  return count
