# 22_ChallengeAdvLists2_RemoveMiddle
# hakon.code@gmail.com

def remove_middle(my_list, start, end):
  beginning = my_list[:start]
  ending = my_list[end+1:]
  return beginning + ending
  

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))