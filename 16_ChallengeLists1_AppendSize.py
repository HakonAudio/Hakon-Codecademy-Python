# 16_ChallengeLists1_AppendSize
# hakon.code@gmail.com

def append_size(my_list):
  length = len(my_list)
  my_list.append(length)
  return my_list


#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))


# Better way

# def append_size(my_list):
#   my_list.append(len(my_list))
#   return my_list