# 20_ChallengeLists5_CombineSort
# hakon.code@gmail.com

def combine_sort(my_list1, my_list2):
  new_list = my_list1 + my_list2
  new_list.sort()
  return new_list


#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


# Or this:
# def combine_sort(my_list1, my_list2):
#   unsorted = my_list1 + my_list2
#   sortedList = sorted(unsorted)
#   return sortedList








# Completely wrong first take...

# def combine_sort(my_list1, my_list2):
#   new_list = list(zip(my_list1, my_list2))
#   new_list.sort()
#   return new_list


# #Uncomment the line below when your function is done
# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))