# 26_ChallengeLoops_DivisibleByTen
# hakon.code@gmail.com

def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
    else:
      continue
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 50, 25, 30, 35, 40]))



# else not neccessary 

# def divisible_by_ten(nums):
#   count = 0
#   for number in nums:
#     if (number % 10 == 0):
#       count += 1
#   return count
