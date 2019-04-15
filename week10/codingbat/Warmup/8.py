<<<<<<< HEAD
def pos_neg(a, b, negative):
  if negative:
    return(a < 0 and b < 0)
  else:
=======
def pos_neg(a, b, negative):
  if negative:
    return(a < 0 and b < 0)
  else:
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
    return((a<0 and b>0) or (a>0 and b<0))