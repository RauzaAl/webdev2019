<<<<<<< HEAD
def alarm_clock(day, vacation):
  pronto = "7:00" if not vacation else "10:00"
  tarde = "10:00" if not vacation else "off"
=======
def alarm_clock(day, vacation):
  pronto = "7:00" if not vacation else "10:00"
  tarde = "10:00" if not vacation else "off"
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
  return pronto if day not in [6,0] else tarde