# 24_ChallengeAdvLists4_DoubleIndex
# hakon.code@gmail.com

def double_index(my_list, index):
  if index >= len(my_list):
    return my_list
  else:
    double = my_list[index] * 2
  
    new_list = my_list[0:index] + [double] + my_list[index+1:]
    return new_list


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))


# def double_index(my_list, index):
#   # Checks to see if index is too big
#   if index >= len(my_list):
#     return my_list
#   else:
#     # Gets the original list up to index
#     my_new_list = my_list[0:index]
#  # Adds double the value at index to the new list 
#   my_new_list.append(my_list[index]*2)
#   #  Adds the rest of the original list
#   my_new_list = my_new_list + my_list[index+1:]
#   return my_new_list