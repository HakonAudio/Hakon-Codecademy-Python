# 19_ChallengeLists4_MoreThanN
# hakon.code@gmail.com

def more_than_n(my_list, item, n):
  if n < my_list.count(item):
    return True
  else:
    return False


#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))