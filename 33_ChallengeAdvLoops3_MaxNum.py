# 33_ChallengeAdvLoops3_MaxNum
# hakon.code@gmail.com


def max_num(nums):
  max = nums[0]

  for n in nums:
    if n > max:
      max = n
  return max


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))