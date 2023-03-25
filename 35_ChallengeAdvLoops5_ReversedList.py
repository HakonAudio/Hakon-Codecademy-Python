# 35_ChallengeAdvLoops5_ReversedList
# hakon.code@gmail.com

#Write your function here
# def reversed_list(lst1, lst2):
#   rev_lst2 = lst2[::-1]
#   for l1 in lst1:
#     if lst1[l1] == rev_lst2[l1]:
#       return True
#     else:
#       return False

# #Uncomment the lines below when your function is done
# print(reversed_list([1, 2, 3], [3, 2, 1]))
# print(reversed_list([1, 5, 3], [3, 2, 1]))

def reversed_list(lst1, lst2):
  rev_lst2 = lst2[::-1]
  for i in range(len(lst1)):
    if lst1[i] != rev_lst2[i]:
      return False
  return True


# # Official
# def reversed_list(lst1, lst2):
#   for index in range(len(lst1)):
#     if lst1[index] != lst2[len(lst2) - 1 - index]:
#       return False
#   return True