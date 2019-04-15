<<<<<<< HEAD
def sum13(nums):
  while 13 in nums:
    if nums.index(13) < len(nums)-1:
      nums.pop(nums.index(13)+1)
    nums.pop(nums.index(13))
    
  return sum(nums)
=======
def sum13(nums):
  while 13 in nums:
    if nums.index(13) < len(nums)-1:
      nums.pop(nums.index(13)+1)
    nums.pop(nums.index(13))
    
  return sum(nums)
>>>>>>> ec863b8dfbbeba8f5506e1f29976ea8308fddd9e
