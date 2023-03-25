# 17_ChallengeLists2_AppendSum
# hakon.code@gmail.com

def append_sum(my_list):
  counter = 0
  while counter < 3:
    my_list.append(my_list[-1] + my_list[-2])
    counter += 1
  return my_list


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
