# 31_ChallengeAdvLoops1_LargerSum
# hakon.code@gmail.com

#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0

  for s1 in lst1:
    sum1 += s1

  for s2 in lst2:
    sum2 += s2

  if sum1 >= sum2:
    return lst1
  else:
    return lst2




#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# One liner

# def larger_sum(lst1, lst2):
#   return lst1 if sum(lst1) >= sum(lst2) else lst2