# 25_ChallengeAdvLists5_MiddleItem
# hakon.code@gmail.com


def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2


    # count = int(len(my_list))
    # my_list[count]

    
    # lower = my_list[int(len(my_list))]
    # higher
    # return average = (lower + higher) / 2

    # return my_list[int(len(my_list) / 2)]

  else:
    return my_list[int(len(my_list) / 2)]



#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))