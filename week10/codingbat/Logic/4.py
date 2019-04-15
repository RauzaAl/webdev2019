<<<<<<< HEAD
def caught_speeding(speed, is_birthday):

  speeding = speed - (65 if is_birthday else 60)
  if speeding > 20:
    return 2
  elif speeding > 0:
    return 1
  else:
=======
def caught_speeding(speed, is_birthday):

  speeding = speed - (65 if is_birthday else 60)
  if speeding > 20:
    return 2
  elif speeding > 0:
    return 1
  else:
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
    return 0