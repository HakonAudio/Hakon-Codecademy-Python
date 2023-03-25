# 34_ChallengeAdvLoops4_SameValues
# hakon.code@gmail.com

def same_values(lst1, lst2):
  new_list = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      new_list.append(i)

  return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))