# 29_ChallengeLoops4_OddIndices
# hakon.code@gmail.com

def odd_indices(lst):
  new_list = []
  for item in range(len(lst)): 
    if item % 2 == 1:
      new_list.append(lst[item])
      
  return new_list


#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))



# def odd_indices(lst):
#   new_lst = []
#   for index in range(1, len(lst), 2):
#     new_lst.append(lst[index])
#   return new_lst






# First take... this one returns just the odd values, not odd indexed

# def odd_indices(lst):
#   new_list = []
#   for item in lst: 
#     if item % 2 == 1:
#       new_list.append(item)
#       lst = lst[1:]
#     else:
#       continue
      
#   return new_list


# #Uncomment the line below when your function is done
# print(odd_indices([4, 3, 7, 10, 11, -2]))
